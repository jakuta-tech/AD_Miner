class Node:

    # TODO PARSE LABELS HERE
    def __init__(self, id, labels, name, domain, tenant_id, relation_type):
        self.id = id
        self.labels = labels
        self.name = name
        self.domain = str(domain)
        self.tenant_id = tenant_id
        self.relation_type = relation_type

    # Needed to use set() on a list of nodes (to remove duplicates from lists)
    def __hash__(self):
        return hash(self.id)

    def __eq__(self, other):
        if not isinstance(other, Node):
            return NotImplemented
        ret = (
            (self.id == other.id)
            and (self.labels == other.labels)
            and (self.name == other.name)
            and (self.domain == other.domain)
            and (self.tenant_id == other.tenant_id)
            and (self.relation_type == other.relation_type)
        )
        return ret
