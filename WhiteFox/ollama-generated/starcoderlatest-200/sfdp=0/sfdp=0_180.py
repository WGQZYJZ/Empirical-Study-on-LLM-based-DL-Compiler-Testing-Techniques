
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(768, 512)
 
    def forward(self, x1, x2):
        scaled_dot_product = torch.matmul(x1, x2.transpose(-2, -1)) / math.sqrt(x1.shape[-1])
        attention_weights = scaled_dot_product.softmax(dim=-1)
        output = attention_weights.matmul(x2)
        return self.linear(output)


# Initializing the model
m = Model()

# Inputs to the model
q  = torch.randn(1, 768, 300) # query (n x d_k x l_q), where n is batch size and l_q is length of q
kv = torch.randn(256, 768, 300) # key-value (n x d_v x l_kv), where n is batch size and l_kv is length of kv

