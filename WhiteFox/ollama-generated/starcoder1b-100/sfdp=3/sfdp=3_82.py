
class Model(torch.nn.Module):
    def __init__(self, hidden_size=256):
        super().__init__()
        self.scale = torch.Tensor([0.1])  # Initialize a scale tensor
        self.value = torch.randn(1, hidden_size)  # Initialize a value tensor
        self.key = torch.randn(1, hidden_size)  # Initialize a key tensor
        self.dropout = nn.Dropout(p=0.5)
 
    def forward(self):
        scaled_qk = self.scale * self.key.matmul(self.value).softmax(-2)
        dropout_qk = self.dropout(scaled_qk)
        output = dropout_qk.matmul(self.value)
        return output

# Inputs to the model
input_tensor  = torch.randn(1, 3, 64, 64)
m  = Model()
