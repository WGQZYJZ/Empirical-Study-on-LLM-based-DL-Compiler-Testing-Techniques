
class MyModel(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value):
        v1  = torch.matmul(query, torch.transpose(key, -2, -1)) / math.sqrt(query.size(-1)) 
        v3  = v1 + attn_mask
        v4  = torch.softmax(v3, dim=-1) 
        return v4@value

# Initializing the model
m  = MyModel()

 # Inputs to the model
query   = torch.randn(64, 256)
key     = torch.randn(64, 780)
value    = torch.randn(64, 128)

 # Generating attn_mask for attention mechanism
attn_mask = np.ones((query.shape[1], query.shape[1])) 

for i in range(int(key.size(-1))):
    attn_mask[:, -i-1]   *= 0

attn_mask = torch.from_numpy(np.array([attn_mask]))

 # Running the model and getting its output
output = m(query, key, value)
 
 