
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value, dropout_p=0.1):
        v  = torch.nn.functional.dropout(query, p=dropout_p)
        return query


# Initializing the model
m  = Model()

# Inputs to the model