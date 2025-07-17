def build_catalog_number(product_type, selections):
    if product_type == "Non-Illuminated Pushbuttons":
        return f"10250T{selections['Operator']}{selections['Button Color']}-{selections['Circuit']}"
    
    elif product_type == "Non-Illuminated Pushpulls":
        return f"10250T{selections['Operator']}{selections['Button']}{selections['Circuit']}"
    
    elif product_type == "Illuminated Incandescent Pushpulls":
        return f"10250T{selections['Operator']}{selections['Light Unit']}{selections['Lens']}{selections['Circuit']}"
    
    elif product_type == "Illuminated LED Pushpulls":
        return f"10250T{selections['Operator']}{selections['Light Unit']}{selections['Lens']}={selections['Voltage']}{selections['Circuit']}"
    
    elif product_type == "Illuminated Incandescent Pushbuttons":
        return f"10250T{selections['Light Unit']}{selections['Lens']}{selections['Circuit']}"
    
    elif product_type == "Illuminated LED Pushbuttons":
        return f"10250T{selections['Light Unit']}{selections['Lens']}{selections['Voltage']}{selections['Circuit']}"
    
    else:
        return "Invalid product type"
