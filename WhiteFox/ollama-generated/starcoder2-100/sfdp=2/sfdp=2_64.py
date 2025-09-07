
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.dropout = torch.nn.Dropout(p=0)
 
    def forward(self, query, key, value):
        v1  = torch.matmul(query, key.transpose(-2, -1)) # Compute the dot product of a query and a key
        v2  = v1 / inv_scale_factor
        v3  = self.dropout(v2)
        v4  = torch.nn.functional.softmax(v3, dim=-1) 
        return torch.matmul(value, v4)

# Initializing the model
m = Model()

# Inputs to the model
query_tensor  = torch.randn(8, 64)
key_tensor   = torch.randn(512, 64, requires_grad=True).to('cuda')
value_tensor  = torch.randn(8, 64).to('cuda')

 # Initializing a device to load the tensors onto the GPU and activating gradient calculation on this device. 
device = 'cuda' if torch.cuda.is_available() else 'cpu'
query_tensor = query_tensor.clone().detach().requires_grad_(True).to(device)
key_tensor   = key_tensor.clone().detach().requires_grad_(False).to(device) # The key and value tensors should be on CPU, otherwise a RuntimeError will occur when activating gradient calculation.
value_tensor  = value_tensor.clone().detach().requires_grad_(True).to(device)

 