
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value):
        scale = 10000 ** (key.pow(2).mean(-1) - 0.5)
        scaled_qk  = torch.div(query @ key.transpose(-2, -1), scale)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
 
        v  = dropout_qk @ value

        return v


# Initializing the model
m  = Model()
 

# Inputs to the model
query  = torch.randn([1600, 384])
key  = torch.randn([576, 384])
value  = torch.randn([2304, 768])

 # Outputs of the model (first dimension may vary)
__output__  = m(query, key, value).shape  # Output shape is (1600, 768)