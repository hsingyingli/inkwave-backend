from faker import Faker
import pytest
from app.utils.monadic import Fail, Success, async_monadic, monadic

fake = Faker()

def test_monadic_decorator_return_success_when_return_value():
    return_value = fake.name

    @monadic
    def foo():
        return return_value 


    result = foo()

    assert type(result) == Success
    assert result.is_succeeded == True 
    assert result.is_failed == False 
    assert result.errors is None 
    assert result.result == return_value

def test_monadic_decorator_return_fail_when_return_fail():
    return_value = fake.name

    @monadic
    def foo():
        return Success(result=return_value)


    result = foo()

    assert type(result) == Success
    assert result.is_succeeded == True 
    assert result.is_failed == False 
    assert result.errors is None 
    assert result.result == return_value

def test_monadic_decorator_return_fail_when_raise_exception():

    @monadic
    def foo():
        raise Exception()


    result = foo()

    assert type(result) == Fail
    assert result.is_succeeded == False
    assert result.is_failed == True
    assert type(result.errors) == Exception
    assert result.result is None 

def test_monadic_decorator_return_success_when_return_success():
    return_value = fake.name

    @monadic
    def foo():
        return Fail(errors=return_value)


    result = foo()

    assert type(result) == Fail
    assert result.is_succeeded == False
    assert result.is_failed == True
    assert result.errors == return_value
    assert result.result is None

@pytest.mark.asyncio
async def test_async_monadic_decorator_return_success_when_return_value():
    return_value = fake.name

    @async_monadic
    async def foo():
        return return_value 


    result = await foo()

    assert type(result) == Success
    assert result.is_succeeded == True 
    assert result.is_failed == False 
    assert result.errors is None 
    assert result.result == return_value

@pytest.mark.asyncio
async def test_async_monadic_decorator_return_fail_when_return_fail():
    return_value = fake.name

    @async_monadic
    async def foo():
        return Success(result=return_value)

    result = await foo()

    assert type(result) == Success
    assert result.is_succeeded == True 
    assert result.is_failed == False 
    assert result.errors is None 
    assert result.result == return_value

@pytest.mark.asyncio
async def test_async_monadic_decorator_return_fail_when_raise_exception():

    @async_monadic
    async def foo():
        raise Exception()


    result = await foo()

    assert type(result) == Fail
    assert result.is_succeeded == False
    assert result.is_failed == True
    assert type(result.errors) == Exception
    assert result.result is None 

@pytest.mark.asyncio
async def test_async_monadic_decorator_return_success_when_return_success():
    return_value = fake.name

    @async_monadic
    async def foo():
        return Fail(errors=return_value)


    result = await foo()

    assert type(result) == Fail
    assert result.is_succeeded == False
    assert result.is_failed == True
    assert result.errors == return_value
    assert result.result is None
