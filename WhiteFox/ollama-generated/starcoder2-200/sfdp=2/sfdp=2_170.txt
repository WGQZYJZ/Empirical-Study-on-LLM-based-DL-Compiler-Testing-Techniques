
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value, dropout_p=0., inv_scale_factor=1.0):
        v  = torch.nn.functional.dropout(torch.nn.functional.softmax(query), p=dropout_p)
        v2 = v @ value * 3 + 4 - 5 - query
        return v2


# Initializing the model