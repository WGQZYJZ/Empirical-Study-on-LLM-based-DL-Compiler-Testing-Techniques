in1_features = 2
in2_features = 3
out_features = 4
input1 = torch.randn(1, in1_features)
input2 = torch.randn(1, in2_features)
bilinear = torch.nn.Bilinear(in1_features, in2_features, out_features)
output = bilinear(input1, input2)