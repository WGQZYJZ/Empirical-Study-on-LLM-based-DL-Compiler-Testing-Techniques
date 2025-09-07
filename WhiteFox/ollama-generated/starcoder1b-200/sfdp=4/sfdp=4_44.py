
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query  = torch.nn.Linear(3, 4)
        self.key    = torch.nn.Linear(3, 4)
        self.value  = torch.nn.Linear(3, 4)
        self.attn_mask = torch.zeros((1, 4))
 
    def forward(self, x1, x2):
        # Query
        query = self.query(x1)
        # Key
        key = self.key(x2)
        # Value
        value = self.value(x2)
 
        attn_mask = (1 - self.attn_mask).type(torch.float32)  # For the dot product of two tensors, we need to mask out attention to positions where input tensor `query` is empty or not in batch mode
        attn_weight = torch.softmax(query @ key / math.sqrt(query.size(-1)), dim=-1)  # Use the softmax function to scale the dot product of query and key
        output = attn_weight @ value  # Compute the weighted sum of the values
 
        return output


# Initializing the model
m = Model()


