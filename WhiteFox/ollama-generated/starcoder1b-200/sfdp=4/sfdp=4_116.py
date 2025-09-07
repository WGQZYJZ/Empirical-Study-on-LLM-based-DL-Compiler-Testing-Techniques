
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(3, 8) # Initialize the query and key as linear layers with output size 8
        self.key   = torch.nn.Linear(8, 8)
        self.value = torch.nn.Linear(8, 16)
 
    def forward(self, x1):
        qk = self.query(x1).view(-1, 3, -1) # Compute the scaled dot product between the query and key tensors
        k   = self.key(x1).view(-1, 8, -1) # Extract the hidden representation of each query dimension (dim=-1)
        v   = self.value(x1).view(-1, 16, -1) # Extract the hidden representation of each key dimension (dim=-1)
        qk *= math.sqrt(qk.size(-1))  # Scale the dot product to avoid division by zero
        attn_weight = torch.softmax(qk, dim=-1)  # Apply softmax to the scaled dot product output between the query and key tensors
        out   = attn_weight @ v  # Compute the weighted sum of the value tensor with the result from the weighted sum computation in the attention mechanism
        return out


# Initializing the model
m = Model()

