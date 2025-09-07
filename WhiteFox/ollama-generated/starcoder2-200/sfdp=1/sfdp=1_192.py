
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.randn(1, 8)
        self.key = torch.randn(1, 2048)
        self.value = torch.randn(1, 5000)
        self.scale_factor = torch.rand(1) * 6e-7  # scale factor
        self.dropout_p = torch.rand(1) / 3 + .01

    def forward(self, query):
        v1 = torch.matmul(query, self.key.transpose(-2, -1))
        v2 = v1.div(self.scale_factor).softmax(dim=-1) # This is a softmax with logits, which is the proper form
        v3 = torch.nn.functional.dropout(v2, p=self.dropout_p)
        return v3.matmul(self.value),


# Initializing the model
m = Model()


# Inputs to the model
query  = torch.randn(100, 8)

## Note: The inputs are not fixed! This means that you should generate different queries and keys for each input tensor `query`. 
