
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.key = torch.nn.Parameter(torch.empty(30, 20)) # Size of 30x20 is arbitrary 
        self.value = torch.nn.Parameter(torch.empty(45, 18)) # Size of 45x18 is arbitrary 
        self.query = torch.nn.Parameter(torch.empty(76, 19))# Size of 76x19 is arbitrary
        self.scale_factor = float(self.key.shape[0])**-0.5 # The scaling factor that we use is the square root of the size of key tensor

    def forward(self):
        scaled_dot_product = torch.matmul(query, key.transpose(-2,-1))/self.scale_factor  # In our example, these tensors are 30x45, 76x45 and 30x19 matrices respectively, with dimension of 45.
        attention_weights = scaled_dot_product.softmax(dim=-1) 
        return torch.bmm(attention_weights, value) # In our example these tensors are 76x45, 76x18 and 30x19 matrices respectively

# Initializing the model
m  = ScaledDotProductAttention()
__output__  = m()

