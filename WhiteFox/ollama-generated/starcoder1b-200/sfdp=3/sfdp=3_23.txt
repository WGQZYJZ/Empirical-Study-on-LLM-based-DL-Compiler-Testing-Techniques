
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        # The model contains two branches of parameters
        # One for the weight and one for the bias
        w = self.conv.weight
        b = self.conv.bias
 
        v1 = torch.matmul(x1, w.transpose(-2, -1))  # Apply dot product to the inputs
        v2 = v1 * scale_factor  # Scale the output of the previous step
        v3 = torch.nn.functional.relu(v2 + b)  # Relu applied before adding bias to the input
        qk = torch.matmul(v3, k.transpose(-2, -1))  # Compute dot product between inputs and weights
        s = softmax_qk * dropout_p
        v4 = qk.matmul(v3)  # Apply dot product on the output of step 4

        output = v4 * scale_factor + b  # Add bias to output from step 2
        return output


# Initializing the model
m = Model()

