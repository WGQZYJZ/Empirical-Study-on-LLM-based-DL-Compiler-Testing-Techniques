v1 = torch.nn.functional.pad(conv(x2), pad=((0, 3), (0, 3), (0, 3), (0, 3)), value=1)(x1) * 50 / 49672
