
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, query, key, value):

        v1 = torch.matmul(query, key) / 0.25
        v3 = torch.softmax(v1, dim=-1)
        v4 = v3 * value

# Initializing the model
m = Model()

 # Inputs to the model
query_input = torch.randn(1, 64)
key_input  = torch.randn(1, 800)
value_input = torch.randn(1, 32)
 
 # The model should be different from the previous one
__output__m(query_input, key_input, value_input)


