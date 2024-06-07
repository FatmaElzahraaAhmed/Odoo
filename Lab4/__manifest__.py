{
    'name': 'Custom Sale Order Enhancements',
    'version': '1.0',
    'depends': ['sale', 'web'],
    'data': [
        'views/sale_order_view.xml',
        'report/sale_order_report.xml',
        'security/security.xml',
        'security/ir.model.access.csv',
    ],
}
