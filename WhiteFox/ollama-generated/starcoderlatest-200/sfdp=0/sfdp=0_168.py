
class Attention(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention_layer = torch.nn.Linear(768, 3072)
 
    def forward(self, q1, k1, v1):
        # The scaled dot product of the query and key tensor are obtained as the output of an linear layer with a dimension 3072.
        attention_weights = torch.nn.functional.softmax(self.attention_layer(torch.cat([q1, k1], dim=-1)), dim=-1)
 
        # The final outputs of the attention mechanism are obtained by multiplying the weighted sum of the value tensor and the weights for each time step together with a linear layer to get the output tensors.
        output = self.attention_layer(torch.cat([v1, torch.mul(v1, attention_weights)], dim=-2))
 
        return output
 
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.conv1  = torch.nn.Conv2d(3, 64, 7, stride=2, padding=0)
        self.bn1    = torch.nn.BatchNorm2d(64)
        self.relu   = torch.nn.ReLU()
 
        self.conv2  = torch.nn.Conv2d(64, 128, 3, stride=2, padding=1)
        self.bn2    = torch.nn.BatchNorm2d(128)
        self.relu   = torch.nn.ReLU()
 
        self.conv3  = torch.nn.Conv2d(128, 768, 3, stride=1, padding=0)
 
    def forward(self, x1):
        # A series of Conv, BatchNorm, ReLU layers for each convolution and batch normalization respectively are conducted with a stride of 2 and zero padding. The output tensor obtained after the last layer is 768 dimensional.
        t1 = self.conv1(x1)
        t2 = self.bn1(t1)
        t3 = self.relu(t2)
 
        t4 = self.conv2(t3)
        t5 = self.bn2(t4)
        t6 = self.relu(t5)
 
        # A linear layer is used to conduct a convolution with the output of the last 2 Conv layers and get the attention weights for each time step together. The attention weights are computed as softmax in the dimension specified by the second parameter -1.
        t7 = torch.nn.functional.softmax(self.attention_layer(torch.cat([t6, t3], dim=-1)), dim=-1)
 
        # Another series of Conv, BatchNorm, ReLU layers are conducted with a stride of 1 and zero padding to get the final outputs for each time step together.
        output = torch.nn.functional.conv2d(t7, self.conv3(t6), stride=1)
 
        return output
# Initialize the model
m = Model()
 
# Input tensor for the model
x1 = torch.randn(1, 3, 64, 64)
