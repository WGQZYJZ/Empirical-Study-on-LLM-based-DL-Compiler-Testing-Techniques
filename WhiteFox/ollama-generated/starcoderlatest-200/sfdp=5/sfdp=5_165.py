
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(768, 300)
        self.linear2 = torch.nn.Linear(300, 768)
 
    def forward(self, x1, x2):
        v1 = self.linear1(x1) # Linear layer with input size of the first tensor and output size of the second tensor
        v2 = torch.dropout(torch.relu(v1), dropout_p, True) # Dropout operation
        v3  = self.linear2(v2) # The linear layer has no additional parameters and uses the same input and output dimensions as v1
        v4 = torch.dropout(torch.softmax(v3, dim=-1), dropout_p, False) # The softmax operation applies to each column of the result of linear layer
        v5 = self.linear2(v4) # Use dropout layer again
        output = v5
        return output


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 768, 64, 64)
x2 = torch.randn(1, 300, 64 * 64) # The second tensor should be a reshaped result of linear layer in forward function
