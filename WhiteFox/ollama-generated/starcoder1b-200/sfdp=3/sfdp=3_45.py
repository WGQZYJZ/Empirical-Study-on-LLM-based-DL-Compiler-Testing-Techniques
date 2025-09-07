
# Data Augmentation

# Convolution With Zero Padding
The model should contain the following pattern:

# Model
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.bn1 = torch.nn.BatchNorm2d(8)
        self.conv2 = torch.nn.Conv2d(8, 16, 1, stride=2, padding=0)
        self.bn2 = torch.nn.BatchNorm2d(16)
        self.conv3 = torch.nn.Conv2d(16, 32, 1, stride=2, padding=0)
        self.bn3 = torch.nn.BatchNorm2d(32)
 
    def forward(self, x1):
        conv_t1 = self.conv1(x1)
        conv_pad_t1 = torch.nn.functional.pad(conv_t1, ((0, 0), (0, 0), (0, 0), (input_padding, input_padding)), mode='constant', value=1)
        conv_pad_t2 = conv_pad_t1 * 0.5
        return torch.relu(torch.matmul(conv_pad_t2, torch.tanh(self.dropout_rate * conv_t1))))
