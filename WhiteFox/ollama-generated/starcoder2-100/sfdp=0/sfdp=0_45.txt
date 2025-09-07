
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.embed = torch.nn.Embedding(30522, 768)
        self.linear = torch.nn.Linear(768, 4139)
 
    def forward(self, x):
        v1  = self.embed(x[:, :, 0]) 
        v2  = self.embed(x[:, :, 1])
        scaled_dot_product  = v1 @ (v2.transpose(-2,-1)) / math.sqrt(768)   
        attention_weights  = scaled_dot_product.softmax(dim=-1)
        output  = attention_weights @ v2 
        return self.linear(output)
