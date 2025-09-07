
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.qk = torch.nn.Linear(64, 128)

    def forward(self, query, key, value):

        scale_factor = self.qk(query).sigmoid() + 0.5 # Apply a sigmoid function and then add 0.5 to it
        self.scale_factor.data[...] = scale_factor  # Store the inverse scale factor in the model object.
        
        qk = torch.matmul(self.scale_factor, key.transpose(-2,-1))

        return torch.nn.functional.dropout(qk, p=0.3) * value

# Initializing the model and setting the random seed for PyTorch
m  = Model()
torch.manual_seed(4957806) # 0x1D6A42

