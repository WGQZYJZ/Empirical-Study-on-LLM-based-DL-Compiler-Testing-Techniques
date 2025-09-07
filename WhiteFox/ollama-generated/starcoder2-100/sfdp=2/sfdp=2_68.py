
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v3  = torch.nn.functional.dropout(torch.softmax(x2, dim=-1), p=0.75)
        return v4


# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(2, 64) # Shape: [batch_size, num_of_query]
x2  = torch.randn(3, 512) # Shape: [num_of_key, size_of_each_key]


