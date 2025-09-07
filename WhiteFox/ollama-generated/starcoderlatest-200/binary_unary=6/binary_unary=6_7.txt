
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 - other
        v3 = torch.nn.functional.relu(v2)
        return v3
# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
__output__  = m(x1)


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        #v2 = v1 - other
        v3 = torch.nn.functional.relu(v1 + 1)
        return v3


class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(64, 128)
 
    def forward(self, x1):
        #v2 = v1 - other
        v3 = torch.nn.functional.relu(v1 + 1)
        return v3


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 64, 5, stride=1, padding=0)
 
    def forward(self, x1):
        v2 = v1 + 1
        return v3


class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(64, 128)
 
    def forward(self, x1):
        #v2 = v1 - other
        #v3 = torch.nn.functional.relu(v1 + 1)
        v4 = (v1 * 2) ** 0.5
        return v4


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 64, 5, stride=1, padding=0)
 
    def forward(self, x1):
        v2 = (v1 + 1) ** 0.5
        return v4


class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(64, 128)
 
    def forward(self, x1):
        #v2 = (v1 + 1) ** 0.5
        #v3 = torch.nn.functional.relu(v1 + 1)
        v4 = (v1 * 2) ** 0.5
        return v4


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 64, 5, stride=1, padding=0)
 
    def forward(self, x1):
        v2 = (v1 + 1) ** (1/2)
        return v4


class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(64, 128)
 
    def forward(self, x1):
        #v2 = (v1 + 1) ** 0.5
        #v3 = torch.nn.functional.relu(v1 + 1)
        v4 = (v1 * 2) ** 0.5
        return v4


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 64, 5, stride=1, padding=0)
 
    def forward(self, x1):
        v2 = (v1 + 1) ** (0.5/2)
        return v4


class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(64, 128)
 
    def forward(self, x1):
        #v2 = (v1 + 1) ** 0.5
        #v3 = torch.nn.functional.relu(v1 + 1)
        v4 = (v1 * 2) ** 0.5
        return v4


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 64, 5, stride=1, padding=0)
 
    def forward(self, x1):
        v2 = (v1 + 1) ** (-1/2)
        return v4


class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(64, 128)
 
    def forward(self, x1):
        #v2 = (v1 + 1) ** 0.5
        #v3 = torch.nn.functional.relu(v1 + 1)
        v4 = (v1 * 2) ** 0.5
        return v4


class Model(torch.nn.Module):
    def __init__(self): Error executing cp sp sp sp sp sp sp sp sp sp sp sp sp sp sp sp sp sp sp sp sp sp sp sp sp sp sp sp sp sp sp sp