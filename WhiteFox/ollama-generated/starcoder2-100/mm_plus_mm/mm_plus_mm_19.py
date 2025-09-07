
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.mm1  = torch.nn.Linear(50, 2)
        self.mm2  = torch.nn.Linear(347890, 100)
 
    def forward(self, x1, x2):
        v1  = torch.mm(x1, self.mm1.weight.T).clamp(-3., 3.) + self.mm1.bias # Matrix multiplication between x1 and mm1.weight transposed. Then add the bias to the output of the multiplication followed by a clamp operation
        v2  = torch.mm(self.mm2.weight, x2) + self.mm2.bias # Matrix multiplication between mm2.weight and x2. Then add the bias to the output of the multiplication followed by a clamp operation 
        v3  = v1 * 0.5
        v4  = torch.sigmoid(v3) # Apply the sigmoid function to the matrix product of the previous two steps, that is, the first matrix multiplication between x1 and mm1.weight transposed
        v5  = torch.tanh(v2) + 5 * 0.7853981633974483 # Apply the tanh function to the second matrix multiplication of the previous steps, that is, multiplying x2 by mm2.weight, add the bias to the output of the multiplication followed by a scalar multiplication with pi/2 (0.7853981633974483)
        v6  = torch.matmul(v4, v5) # Matrix multiplication between the result of the first matrix multiplication and the second one
        return v6


# Initializing the model