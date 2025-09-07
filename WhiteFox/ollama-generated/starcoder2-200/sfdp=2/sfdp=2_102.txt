
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.matmul  = torch.nn.functional.linear
 
    def forward(self, query):
        v1  = torch.matmul(query, key)
        v2  = v1.div(inv_scale_factor)
        v3  = v2.softmax(-1)
        v4  = dropout(v3, p=dropout_p)
        return v4

# Initializing the model
m  = Model()


# Inputs to the model