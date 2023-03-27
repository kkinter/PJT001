from django.template.defaulttags import register

@register.filter
def get_dict_val(dictionary, key, key_as_str=True):
    if not isinstance(dictionary, dict):
        return None
    if key_as_str:
        key = f"{key}"
    return dictionary.get(key)

@register.filter
def get_object_rating(user, object_id):
    # Rating.object.get(user=user, object_id=object_id) 너무 많은 시간이 걸리는 방법
    pass

