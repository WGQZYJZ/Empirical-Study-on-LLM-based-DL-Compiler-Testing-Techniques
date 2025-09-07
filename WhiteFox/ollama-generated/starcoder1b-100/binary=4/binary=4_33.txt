
class ResNet(torch.nn.Module):
    def __init__(self, block, num_blocks):
        super().__init__()
 
        self.conv1 = torch.nn.Conv2d(3, 6, 3, stride=2, padding=1)
        self.bn1 = torch.nn.BatchNorm2d(6)
 
        for i in range(num_blocks - 2):
            block = block(64 if i == 0 else block.expansion, 1)
            self.add_(self._make_layer(block, 256))
        self.pool = torch.nn.MaxPool2d(2)
 
        self.conv2 = torch.nn.Conv2d(256, 128, 3, stride=1, padding=0)
        self.bn2 = torch.nn.BatchNorm2d(128)
 
        for i in range(num_blocks - 2):
            block = block(128 if i == 0 else block.expansion, 2)
            self.add_(self._make_layer(block, 512))
        self.drop_out = torch.nn.Dropout(0.5)
 
        self.fc = torch.nn.Linear(512, 10)
 
    def _make_layer(self, block, num_layers):
        layers = [block(self.expansion, i == 0 and num_layers or block.expansion) for i in range(num_layers)]
        return torch.nn.Sequential(*layers)
 
    def forward(self, x1):
        out = self.pool(self.conv2(self._relu(self.bn1(self.conv1(x1)))))
 
        out = self.drop_out(out)
        for _ in range(5):
            out = F.leaky_relu_(self.bn2(self.fc(self.drop_out(out)))))
        return out
 
    def _relu(self, x):
        return torch.nn.functional.relu(x)
# Initializing the model
m = ResNet(BasicBlock, 4)
