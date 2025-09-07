
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = torch.nn.Linear(1000, 2)
 
    def forward(self, x1, x2):
        scaled_dot_product = torch.matmul(x1, x2.transpose(-2, -1)) / (sqrt(float(x1.shape[0])) * sqrt(float(x2.shape[0])))
        attention_weights = scaled_dot_product.softmax(dim=-1)
        return self.fc(attention_weights.matmul(x2))


# Inputs to the model
input1  = torch.randn(4, 3, 56, 56)
input2  = torch.randn(4, 8, 1024, 1024)
