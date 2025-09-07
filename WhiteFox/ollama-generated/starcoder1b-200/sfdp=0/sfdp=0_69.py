
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(8, 16, 1, stride=1, padding=1)
        self.fc = torch.nn.Linear(16, 1)
 
    def forward(self, x):
        q_tensor = self.conv1(x)  # Apply pointwise convolution with kernel size 1 to the input tensor
        k_tensor = self.conv2(q_tensor)  # Apply pointwise convolution with kernel size 1 to the input tensor
        v_tensor = torch.exp(k_tensor * key_scale + bias)  # Compute exp(Kx^Tq)
        sdp = torch.matmul(query, k_tensor.transpose(-2, -1)) / inv_scale  # Compute Scaled Dot-Product
        attention_weights = sdp.softmax(dim=-1)  # Compute the softmax of Scaled Dot-Product
        v = attention_weights.matmul(value)  # Multiply weighted sum by the output of the dot product and add bias to get the final output tensor
        return torch.tanh(self.fc(v))


# Initializing the model
m = Model()

