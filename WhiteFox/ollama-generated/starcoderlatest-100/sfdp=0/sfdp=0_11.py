
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Parameter(torch.randn(128, 128))
        self.key = torch.nn.Parameter(torch.randn(128, 64))
 
    def forward(self, x):
        scaled_dot_product = torch.matmul(x, self.query) / math.sqrt(32 * 32)
        attention_weights = F.softmax(scaled_dot_product, dim=-1)
        output = attention_weights.matmul(self.key)
        return output
 
 # Initializing the model
 m = Model()

 # Inputs to the model
 x = torch.randn(64, 32, 32)
 