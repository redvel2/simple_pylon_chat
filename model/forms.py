import formencode

class EmailForm(formencode.Schema):
    allow_extra_fields = True
    filter_extra_fields = True
    email = formencode.validators.Email(not_empty=True)
    name = formencode.validators.String(not_empty=True, max_length=20)
    password=formencode.validators.String(not_empty=True, max_length=20)
class SignInForm(formencode.Schema):
    allow_extra_fields = True
    filter_extra_fields = True
    email = formencode.validators.Email(not_empty=True)
    password=formencode.validators.String(not_empty=True, max_length=20)