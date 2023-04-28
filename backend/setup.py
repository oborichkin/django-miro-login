import setuptools

setuptools.setup(
    name="template",
    packages=setuptools.find_packages(),
    version="0.1.0",
    description="Python project template",
    author="Pavel Oborin",
    author_email="oborin.p@gmail.com",
    url="https://github.com/Oborichkin/python-template",
    python_requires=">=3.6",
    install_requires=[
        "python-dotenv",
        "django==3.2",
        "django-cors-headers",
        "djangorestframework<=3.11.0",
        "djangorestframework_jwt",
        "django-rest-auth",
        "markdown",
        "django-filter",
        "django-allauth @ git+https://github.com/oborichkin/django-allauth.git@miro#egg=django-allauth",
    ],
)
