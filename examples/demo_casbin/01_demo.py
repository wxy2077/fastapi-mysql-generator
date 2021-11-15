"""

主要参考官方readme


"""

import casbin

e = casbin.Enforcer('./model.conf', "./policy.csv", True)

sub = "nick"  # the user that wants to access a resource.
obj = "data1"  # the resource that is going to be accessed.
act = "read"  # the operation that the user performs on the resource.

# 添加
# e.add_policy("alice", "data1", "read")
# e.remove_policy("nick", "data1", "read")


if e.enforce(sub, obj, act):
    # permit alice to read data1casbin_sqlalchemy_adapter
    print("通过")
else:
    # deny the request, show an error
    print("拒绝")
