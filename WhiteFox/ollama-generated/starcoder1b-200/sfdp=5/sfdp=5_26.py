
class Model(torch.nn.Module):
    def __init__(self, attn_dropout=0.25):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.bn1 = torch.nn.BatchNorm2d(8)
        self.conv2 = torch.nn.Conv2d(8, 8, 3, stride=1, padding=1)
        self.bn2 = torch.nn.BatchNorm2d(8)
        self.dropout1 = torch.nn.Dropout(attn_dropout)
        self.dropout2 = torch.nn.Dropout(attn_dropout)
 
    def forward(self, x1):
        v1  = self.conv1(x1)
        v1  = self.bn1(v1)
        v1  = F.relu(v1)
 
        v2  = self.conv2(v1)
        v2  = self.bn2(v2)
        v2  = F.relu(v2)
 
        attn_weight  = torch.softmax(self.dropout1(torch.mm(v2, x1)), dim=-1)
        attn_weight = self.dropout2(attn_weight)
        output  = torch.matmul(attn_weight, x1)
        return output

# Initializing the model
m = Model()

