
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn_head = torch.nn.Linear(256, 128)
 
    def forward(self, qk):
        v1 = qk @ value.transpose(-2, -1) / math.sqrt(query.size(-1))
        attn_weight = torch.softmax(v1, dim=-1)
        output = attn_weight * value
        return output
 
# Initializing the model
m = Model()


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 30, 5)
 
    def forward(self, x1):
        h = F.relu(F.max_pool2d(self.conv1(x1), kernel_size=3))
        return h
 
# Initializing the model
m = Model()


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(288, 10)
 
    def forward(self, x1):
        h = F.relu(F.max_pool2d(self.conv2(x2), kernel_size=3))
        return self.classifier(h)
 
# Initializing the model
m = Model()


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.dropout = torch.nn.Dropout(0.5)
 
    def forward(self, x1):
        return self.dropout(x1)
 
# Initializing the model
m = Model()


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.bnorm = torch.nn.BatchNorm2d(10)
 
    def forward(self, x1):
        return self.bnorm(x1)
 
# Initializing the model
m = Model()


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(64, 30, kernel_size=5, stride=1)
 
    def forward(self, x1):
        h = F.relu(F.max_pool2d(self.conv(x1), kernel_size=3))
        return self.bnorm(h)
 
# Initializing the model
m = Model()


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.bnorm = torch.nn.BatchNorm2d(10)
 
    def forward(self, x1):
        return F.relu(F.max_pool2d(x1, kernel_size=3))
 
# Initializing the model
m = Model()


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(784, 200)
 
    def forward(self, x1):
        return F.relu(self.bnorm(x))
 
# Initializing the model
m = Model()


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.dropout = torch.nn.Dropout2d(0.5)
 
    def forward(self, x1):
        return F.relu(F.max_pool2d(x1, kernel_size=3))
 
# Initializing the model
m = Model()


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.bnorm = torch.nn.BatchNorm2d(30)
 
    def forward(self, x1):
        return F.relu(F.max_pool2d(x1, kernel_size=3))
 
# Initializing the model
m = Model()


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.bnorm = torch.nn.BatchNorm2d(30)
 
    def forward(self, x1):
        return F.relu(F.max_pool2d(x1, kernel_size=3))
 
# Initializing the model
m = Model()


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.bnorm1 = torch.nn.BatchNorm2d(30)
 
    def forward(self, x1):
        return F.relu(F.max_pool2d(x1, kernel_size=3))
 
# Initializing the model
m = Model()


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(64, 30, kernel_size=5, stride=1)
 
    def forward(self, x1):
        h = F.relu(F.max_pool2d(self.conv(x1), kernel_size=3))
        return self.bnorm1(h)
 
# Initializing the model
m = Model()


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(7802, 