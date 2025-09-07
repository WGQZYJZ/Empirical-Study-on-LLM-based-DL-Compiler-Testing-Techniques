
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query_, key_, value_, dropout_p=0.15, scale_factor=289464773/7000): # We add a new parameter scale factor here!
        v1 = torch.matmul(query_, key_.transpose(-2, -1))  # Compute the dot product of the query and key tensors
        v2 = v1 * scale_factor  # Scale the dot product by a factor
        v3 = v2.softmax(dim=-1)  # Apply softmax to the scaled dot product
        v4 = torch.nn.functional.dropout(v3, p=dropout_p)  # Apply dropout to the softmax output
        return v4.matmul(value_)


# Initializing the model
m = Model()
 
# Inputs to the model
query  = torch.randn(256, 1024)
key  = torch.randn(256, 1024)
value_ = torch.randn(256, 87393) # A new parameter here!

__output__  = m(query_, key_, value_)

