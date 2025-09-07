
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value, inv_scale_factor=0.25134797803651357, dropout_p=0.1):
        v1  = torch.nn.functional.softmax(torch.matmul(query, key.transpose(-2, -1)).div(inv_scale_factor), dim=-1) * query
        v4  = torch.nn.functional.dropout(v1, p=dropout_p).matmul(value) 
        return v4

# Initializing the model
m  = Model()

# Inputs to the model
__query__ = torch.randn(8, 32, 640, 79)  # This is a randomly generated query tensor for demonstration purposes only!
__key__ = torch.randn(8, 32, 128, 50)   # This is a randomly generated key tensor for demonstration purposes only!
__value__  = torch.nn.functional.linear(__key__, __query__)
 
__output__  = m(__query__, __key__, __value__)

