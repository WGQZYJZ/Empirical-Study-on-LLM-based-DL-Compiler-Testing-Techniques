

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.query  = torch.nn.Linear(768, 128)
        self.key   = torch.nn.Linear(768, 4096) 
        self.value = torch.nn.Linear(768, 512)
 
 
    def forward(self, x):
 
        query_weights = self.query(x) # Compute the query weights by multiplying the inputs and the query tensor
        key_weights   = self.key(x).permute(-2,-1)# Compute the key weights by multiplying the inputs and transposed the key tensor
        scaled_qk     = query_weights  .mul_(0.7)
        attention      = scaled_qk/torch.norm(scaled_qk, dim=-1, keepdim=True) 
        value_weights  = self.value(x).transpose(-2,-1)
        dropout        = torch.nn.functional.dropout(attention, p=0.85)
        v_d_w          = value_weights.matmul(dropout)
        return v_d_w


# Initializing the model
m  = Model()
 
# Input to the model
x1 = torch.randn(47, 32, 768)

# Generating output from the model
