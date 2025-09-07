
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query):
        key = torch.randn((16 * 32, 48))
        value = torch.randn((16 * 32, 50))

        inv_scale_factor = torch.rand(key.size(-2)).sqrt() * 0.1

        dropout_p = 0.5
        scaled_qk = key.div(inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(value)

        return output


# Initializing the model
m  = Model()

# Inputs to the model
__input__ = torch.randn(16, 32, 48) # query
__output__  = m(__input__)
 

System: You are a source code analyzer for PyTorch.
User: 