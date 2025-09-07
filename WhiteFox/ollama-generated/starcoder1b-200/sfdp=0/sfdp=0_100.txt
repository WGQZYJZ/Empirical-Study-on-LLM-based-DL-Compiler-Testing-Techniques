
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.norm1 = torch.nn.LayerNorm(8)
        self.conv2 = torch.nn.Conv2d(8, 16, 1, stride=1, padding=1)
        self.norm2 = torch.nn.LayerNorm(16)
        self.fc1 = torch.nn.Linear(16 * 5 * 5, 4096)
        self.fc2 = torch.nn.Linear(4096, 4096)
        self.dropout = nn.Dropout(p=0.5)
        self.fc3 = torch.nn.Linear(4096, 1)
    
    def forward(self, x):
        # input_tensor: B x C x H x W
        batch_size, channels, height, width = x.shape
        x = x.view(batch_size * channels, -1).transpose(-2, -1)
        # batch_size * 1 * height * width
        input_tensor = self.conv1(x)  # B x C x 5 x 5
        input_tensor = self.norm1(input_tensor)
        input_tensor = F.relu(input_tensor)
        input_tensor = self.dropout(input_tensor)
        
        input_tensor = input_tensor.view(batch_size, channels, height * width).contiguous()  # B x C x H x W
        input_tensor = input_tensor.transpose(-2, -1)  # B x H x W x C
        input_tensor = self.conv2(input_tensor)  # B x 16 x 5 x 5
        input_tensor = self.norm2(input_tensor)
        input_tensor = F.relu(input_tensor)
        input_tensor = self.dropout(input_tensor)

        x = input_tensor.view(batch_size, -1).contiguous()  # B * C
        x = x.transpose(-2, -1)  # C x B
        x = F.relu(self.fc1(x))  # B x C
        x = self.fc2(x)  # B x C
        return torch.sigmoid(self.fc3(x))


# Initializing the model
m = Model()

