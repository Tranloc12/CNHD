from courses.models import Category, Course, Lesson, Tag, User, Comment
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class BaseSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField(source='image')

    def get_image(self, course):

        if course.image:
            if course.image.name.startswith("http"):
                return course.image.name

            request = self.context.get('request')
            if request:
                return request.build_absolute_uri('/static/%s' % course.image.name)


class CourseSerializer(BaseSerializer):
    class Meta:
        model = Course
        fields = ['id', 'subject', 'created_date', 'updated_date', 'active', 'category', 'image']


class LessonSerializer(BaseSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'subject', 'created_date', 'updated_date', 'image']


class TagSerializer(serializers.ModelSerializer):
    class Meta :
        model = Tag
        fields = ['id','name']


class LessonDetailsSerializer(LessonSerializer):
    tags = TagSerializer(many=True)

    class Meta:
        model =  LessonSerializer.Meta.model
        fields = LessonSerializer.Meta.fields + ['content', 'tags']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fiedls = ['id','username','first_name','last_name']


class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model =Comment
        fields = '__all__'