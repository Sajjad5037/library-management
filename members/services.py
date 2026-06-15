from storage.data import members
from members.models import Member

def create_member(name):

    member = Member(
        id=len(members) + 1,
        name=name
    )

    members.append(member)

    return member  
