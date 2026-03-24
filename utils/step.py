import allure

def step(name):

    def decorator(func):

        def wrapper(*args, **kwargs):

            page = kwargs.get("page") or args[0]

            with allure.step(name):
                result = func(*args, **kwargs)

                allure.attach(
                    page.screenshot(),
                    name=name,
                    attachment_type=allure.attachment_type.PNG
                )

                return result

        return wrapper

    return decorator