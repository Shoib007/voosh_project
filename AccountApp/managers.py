from django.contrib.auth.base_user import BaseUserManager

# class UserManager(BaseUserManager):

#     def create_user(self, username, email, password, **extra_fields):
#         if not username:
#             raise ValueError('The given username must be set')
#         if not password:
#             raise ValueError('The given password must be set')
#         email = self.normalize_email(email)
#         user = self.model(username=username, email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, username, email, password, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)

#         if extra_fields.get('is_staff') is not True:
#             raise ValueError('Superuser must have is_staff=True.')
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError('Superuser must have is_superuser=True.')

#         return self.create_user(username, email, password, **extra_fields)


class UserManager(BaseUserManager):
    use_in_migrations = True
    def create_user(self, email, password, **kwargs):
        if not email:
            raise ValueError('Users must have an email address')    
        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password, **kwargs):
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)
        kwargs.setdefault('is_active', True)
        
        if kwargs.get('is_staff') != True:
            raise ValueError(_('is_staff must be True'))
        if kwargs.get('is_superuser') != True:
            raise ValueError(_('is_superuser must be True'))
        
        return self.create_user(email, password, **kwargs)
    
