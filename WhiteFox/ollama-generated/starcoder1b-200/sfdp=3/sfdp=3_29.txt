
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1d = torch.nn.Conv1d(3, 8, 1, stride=1, padding=0)
        self.conv2d = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)

    def forward(self, x1):
        qk_1 = x1
        scaled_qk_1 = x1
        softmax_qk_1 = scaled_qk_1.softmax(-1)
        dropout_qk_1 = torch.nn.functional.dropout(softmax_qk_1, p=0.2)
        output_1 = dropout_qk_1.matmul(x1)
        
        qk_2 = x1
        scaled_qk_2 = x1
        softmax_qk_2 = scaled_qk_2.softmax(-1)
        dropout_qk_2 = torch.nn.functional.dropout(softmax_qk_2, p=0.3)
        output_2 = dropout_qk_2.matmul(x1)

        return output_1 + output_2


# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(1, 8, 64)
