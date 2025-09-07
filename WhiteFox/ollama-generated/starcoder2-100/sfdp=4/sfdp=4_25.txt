
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.layer  = torch.nn.Linear(1024, 512)
 
    def forward(self, query, key, value, attn_mask=None):
        v1  = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1))
        if attn_mask is not None:
            v1 += attn_mask 
        v2  = torch.softmax(v1, dim=-1)
        return v2 @ value


# Initializing the model
m = Model()
 
 # Inputs to the model
query  = torch.randn(4, 640, 512)
key    = torch.randn(4, 640, 512)
value  = torch.randn(4, 640, 512)

 # Generating the output tensor with model m taking query and key as input. Please make sure the generated model is different from the previous model in terms of weights and hyper-parameters. Also note that the query/key tensors should be of shape (4, 640, 512).
 