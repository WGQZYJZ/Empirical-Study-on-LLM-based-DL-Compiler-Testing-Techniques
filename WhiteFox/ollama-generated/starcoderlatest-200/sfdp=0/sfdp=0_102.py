
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.scaled_dot_product = torch.nn.Linear(768, 320)
 
    def forward(self, x1, x2):
        attention_weights = torch.softmax(
            self.scaled_dot_product(x1), dim=-1
        )
        output = attention_weights.matmul(x2)
        return output


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 768, 512)
x2 = torch.randn(1, 320, 512)
