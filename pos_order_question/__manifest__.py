{
    'name': 'POS Order Questions',
    'version': '17.0.1.0.0',
    'category': 'Point of Sale',
    'summary': 'Add questions related to the product in the session.',
    'description': "This provides an option to add questions related to the "
                   "product in the session at time of ordering.It will help "
                   "you to customize ordering in POS.",
    'author': 'Cybrosys Techno Solutions',
    'company': 'Cybrosys Techno Solutions',
    'maintainer': 'Cybrosys Techno Solutions',
    'website': "https://www.cybrosys.com",
    'depends': ['point_of_sale', 'product'],
    'data': [
        'security/ir.model.access.csv',
        'views/product_template_view.xml'
    ],
    "assets": {
        # Assets
        'point_of_sale._assets_pos': [
            'pos_order_question/static/src/js/PosSession.js',
            'pos_order_question/static/src/js/Popups/OrderQuestionPopup.js',
            'pos_order_question/static/src/xml/Popups/OrderQuestionPopup.xml',
            'pos_order_question/static/src/js/Screens/ProductScreen/Orderline.js',
            'pos_order_question/static/src/xml/Screens/ProductScreen/Orderline.xml',
            'pos_order_question/static/src/css/Popups/OrderQuestionPopup.css',
            'pos_order_question/static/src/js/Screens/ProductScreen/pos_orderline.js'
        ],

    },
    'images': [
        'static/description/banner.jpg',
    ],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
