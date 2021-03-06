from rest_framework import serializers
from .models import HomeWorkInfModel, HomeWorkMembersModel


class HomeWorkUpSerializer(serializers.Serializer):  # 用于登录的表单合法性验证，防止绕过前端验证
    name = serializers.CharField()
    type = serializers.CharField()
    subject = serializers.CharField()
    remark = serializers.CharField(required=False)
    end_time = serializers.CharField()
    member_can_know_donelist = serializers.CharField()
    member_can_see_others = serializers.CharField()
    can_submit_after_end = serializers.CharField()
    def validate_name(self, name):
        if len(name) > 50:
            raise serializers.ValidationError("名称长度过长")
        return name

    def validate_type(self, type):
        types = ['file', 'hypertext']
        if type not in types:
            raise serializers.ValidationError("不支持的类型")
        return type

    def validate_subject(self, subject):
        if len(subject) > 30:
            raise serializers.ValidationError("科目过长")
        return subject

    def validate_remark(self, remark):
        if len(remark) > 500:
            raise serializers.ValidationError("备注过长")
        return remark

    def validate_end_time(self, end_time):
        try:
            int(end_time[0:4])
            int(end_time[5:7])
            int(end_time[8:10])
            int(end_time[11:13])
            int(end_time[14:16])
            return end_time
        except:
            raise serializers.ValidationError("日期格式不正确")


class HomeWorkInfSerializer(serializers.ModelSerializer):
    owner = serializers.SerializerMethodField()
    groups = serializers.SerializerMethodField()

    class Meta:
        model = HomeWorkInfModel
        fields = '__all__'

    def get_owner(self, obj):
        return obj.owner.first_name

    def get_groups(self, obj):
        groups_query = obj.groups.all()
        groups_list = list()
        for group in groups_query:
            group_inf = dict()
            group_inf['id'] = group.id
            group_inf['name'] = group.name
            groups_list.append(group_inf)
        return groups_list


class HomeWorkCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeWorkInfModel
        fields = ['id', 'name', 'end_time', 'owner', 'subject', 'end_time']

    owner = serializers.SerializerMethodField()

    def get_owner(self, obj):
        return obj.owner.first_name


class HomeWorkSerializer(serializers.Serializer):
    id = serializers.SerializerMethodField()
    name = serializers.SerializerMethodField()
    owner = serializers.SerializerMethodField()
    subject = serializers.SerializerMethodField()
    end_time = serializers.DateTimeField()
    done = serializers.BooleanField()

    def get_id(self, obj):
        return obj.work.id

    def get_name(self, obj):
        return obj.work.name

    def get_owner(self, obj):
        return obj.work.owner.first_name

    def get_subject(self, obj):
        return obj.work.subject


class DoneListSerializer(serializers.ModelSerializer):
    owner = serializers.SerializerMethodField()

    class Meta:
        model = HomeWorkMembersModel
        fields = ['id', 'done', 'file_name', 'upload_time', 'owner']

    def get_owner(self, obj):
        return {'name': obj.owner.first_name, 'id': obj.owner.id}
