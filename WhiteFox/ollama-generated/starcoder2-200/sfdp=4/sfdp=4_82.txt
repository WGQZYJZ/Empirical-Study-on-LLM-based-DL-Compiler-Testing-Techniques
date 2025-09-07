

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        q = torch.matmul(x1, x2) / math.sqrt(query.size(-1)) # Compute the dot product of query and key tensors
        attn_mask  = torch.ones(query.shape).to('cuda') * -float('inf') # Create a mask with shape equal to query's shape 
        attn_mask[..., -len(x2):]  = 0 # Set diagonal values to zero so that we can't attend to the value vector
        attn_weight  = torch.softmax(q + attn_mask, dim=-1) # Apply softmax on the result of computing dot product and attention mask 
        output  = torch.matmul(attn_weight, x2) # Compute a weighted sum of values tensor using attention weights 
        return output


# Initializing the model
m  = Model()


# Inputs to the model
x1  = torch.randn([3208576], requires_grad=True).reshape(query.shape[0], query.shape[-1]).to('cuda') # Create a query tensor with shape equal to the previous attention mask's size. 
x2  = torch.randn([34980, 1608576] ).to('cuda') # Create value and key tensors of shape equal to the last shape parameter
__output__  = m(x1, x2)

