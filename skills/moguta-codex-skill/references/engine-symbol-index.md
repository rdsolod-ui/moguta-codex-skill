# Engine symbol index

Snapshot: 2026-07-30. This navigation index lists documented symbol
names only. Read the linked official class page for parameters and return
values, then verify the installed source because the generated reference
can lag behind a specific Moguta.CMS release.

## Contents

- [Global functions](#global-functions)
- [Libraries](#libraries)
- [Models](#models)
- [Controllers](#controllers)
- [Hook names](#hook-names)

Indexed symbols: 795 methods/functions.

## Global functions

### [Функции](https://wiki.moguta.ru/help/metodadapter.html)

`mgAddAction`, `mgAddActionOnce`, `mgAddCustomPriceAction`, `mgAddShortcode`, `mgPageThisPlugin`, `mgActivateThisPlugin`, `mgDeactivateThisPlugin`, `mgCreateHook`, `mgAddMeta`, `mgExcludeMeta`, `setOption`, `getOption`, `mgMenu`, `mgMenuFull`, `mgGetCart`, `mgMeta`, `mgMetaInsertMode`, `mgMetaInsert`, `removePropCode`, `mgSEO`, `mgTitle`, `viewData`, `mgDeclensionNum`, `isStaticPage`, `mgSmallCartBlock`, `mgSearchBlock`, `mgContactBlock`, `mgImageProduct`, `mgImageProductPath`, `mgSubCategory`, `mgGalleryProduct`, `mgLogo`, `layout`, `priceFormat`, `filterCatalog`, `copyrightMoguta`, `backgroundSite`, `isIndex`, `isCatalog`, `isCart`, `isOrder`, `isSearch`, `horizontMenu`, `horizontMenuDisable`, `catalogToIndex`, `mgGetPaymentRateTitle`, `lang`, `mb_basename`, `getHtmlAttributes`, `component`, `maket`

## Libraries

### [Avito](https://wiki.moguta.ru/help/Libraries/Avito.html)

`createPage`, `getCitys`, `getSubways`, `updateDB`, `getCatName`, `buildSelects`, `buildSelectsAdditional`, `getCats`, `updateCatsRecurs`, `saveCat`, `newTab`, `saveTab`, `getTab`, `deleteTab`, `getRelated`, `convertProps`, `convertToRub`, `fixCatNames`, `constructXML`

### [Category](https://wiki.moguta.ru/help/Libraries/Category.html)

`getParentUrl`, `resizeCategoryImg`, `addCategory`, `updateCategory`, `delCategory`, `getCategoriesHTML`, `getCategoriesHorHTML`, `getCategoryListUl`, `getChildCategoryIds`, `getCategoryList`, `getChildsCategory`, `getCategoryTitleList`, `getInsideCategory`, `getHierarchyCategory`, `getTitleCategory`, `moveCategory`, `getCategoryByUrl`, `getCategoryById`, `getUserPropertyCategoryById`, `getPropertyForCategoryById`, `getArrayCategory`, `getDesctiption`, `getImageCategory`, `sort`, `changeSortCat`, `clearCategoryRate`, `applyRateToSubCategory`, `getCategoryCount`, `sortToAlphabet`, `sortToAdd`, `exportToCsv`, `addToCsvLine`, `rowCsvPrintToFile`, `getPages`, `getPagesSimple`, `getHtmlPageRowSimple`, `getHtmlPageRow`, `getFiscalizationSettings`

### [CRYPT](https://wiki.moguta.ru/help/Libraries/CRYPT.html)

`mgCrypt`, `mgDecrypt`, `json_encode_cyr`

### [CSV](https://wiki.moguta.ru/help/Libraries/CSV.html)

`export`

### [DB](https://wiki.moguta.ru/help/Libraries/DB.html)

`buildPartQuery`, `buildQuery`, `fetchAssoc`, `fetchObject`, `fetchArray`, `fetchRow`, `insertId`, `numRows`, `affectedRows`, `createIndexIfNotExist`, `query`, `quote`, `quoteInt`, `quoteFloat`, `quoteIN`, `errorLog`, `console`, `lastQuery`, `idAutoIncrement`, `addAutoIncrement`, `close`, `getMysqlVersion`

### [Delivery](https://wiki.moguta.ru/help/Libraries/Delivery.html)

`getDeliveryById`, `getCostDelivery`

### [EventHook](https://wiki.moguta.ru/help/Libraries/EventHook.html)

`run`, `getHookName`, `getCountArg`, `getPriority`, `getClass`, `getFunctionName`

### [Filter](https://wiki.moguta.ru/help/Libraries/Filter.html)

`getFilterSql`, `getHtmlFilter`, `getHtmlFilterAdmin`, `getHtmlPropertyFilter`, `getHtmlPropertyFilterAdmin`, `getProductIdByFilter`, `getApplyFilterList`

### [GoogleMerchant](https://wiki.moguta.ru/help/Libraries/GoogleMerchant.html)

`createPage`, `updateDB`, `getCatName`, `buildSelects`, `getCats`, `updateCatsRecurs`, `saveCat`, `clearTrash`, `newTab`, `saveTab`, `getTab`, `deleteTab`, `getRelated`, `constructXML`

### [Import](https://wiki.moguta.ru/help/Libraries/Import.html)

`setTypeCatalog`, `setNotUpdateFields`, `getValidError`, `getTitleList`, `startCategoryUpload`, `startUpload`, `stopProcess`, `importFromCsv`, `getCompliance`, `validateFormate`, `formateCategoryMogutaCMS`, `formateMogutaCMS`, `createProduct`, `createCategory`, `parseCategoryPath`, `getCategoryId`, `getProductId`, `parseImgSeo`, `downloadImgFromSite`, `autoStartImageGen`, `log`, `isEndFile`, `updateProduct`

### [MailChimp](https://wiki.moguta.ru/help/Libraries/MailChimp.html)

`createPage`, `saveOptions`, `uploadAll`, `uploadOne`

### [Mailer](https://wiki.moguta.ru/help/Libraries/Mailer.html)

`sendMimeMail`, `setSMTPDataConnect`, `addHeaders`, `mimeHeaderEncode`, `sendMimeMailWithFile`

### [Menu](https://wiki.moguta.ru/help/Libraries/Menu.html)

`getMenuFull`, `getMenu`, `getArrayMenu`

### [MG](https://wiki.moguta.ru/help/Libraries/MG.html)

`addAction`, `addShortcode`, `addPriceCustomFunction`, `addBodyClass`, `addAgreementCheckbox`, `getFilesR`, `rrmdir`, `rMoveDir`, `getPriceCustomFunctions`, `pageThisPlugin`, `activateThisPlugin`, `deactivateThisPlugin`, `createHook`, `createActivationHook`, `createDeactivationHook`, `stripslashesArray`, `getParameter`, `defenderXss`, `defenderXss_decode`, `disableTemplate`, `enableTemplate`, `get`, `getSetting`, `setSetting`, `getConfigIni`, `getHtmlContent`, `inlineEditor`, `modalEditor`, `contextEditor`, `newTableContent`, `getMenu`, `getPhpContent`, `getSmalCart`, `loger`, `createTempDir`, `printGui`, `meta`, `createTemplateColorsCssFile`, `addJsVar`, `mergeStaticFile`, `externalJsLinksException`, `clearMergeStaticFile`, `copyImagesFiles`, `set`, `setDifinePathTemplate`, `templateData`, `templateFooter`, `getBuffer`, `printTemplate`, `titlePage`, `seoMeta`, `translitIt`, `redirect`, `setOption`, `getOption`, `declensionNum`, `addInformer`, `createInformerPanel`, `prioritet`, `textMore`, `changeRowsTable`, `logReffererInfo`, `saveUTM`, `clearUTM`, `getUTM`, `dateConvert`, `isMobileDevice`, `layoutManager`, `numberFormat`, `numberDeFormat`, `roundPriceBySettings`, `priceCourse`, `nl2br`, `genRandomWord`, `replaceBBcodes`, `prepareLangData`, `saveLocaleData`, `loadLocaleData`, `removeLocaleDataByEntity`, `cloneLocaleData`, `checkProductOnStorage`, `getMainStorage`, `checkStorageOnOrderCreate`, `decreaseCountProductOnStorage`, `loadCountFromStorageToCatalog`, `loadWholeSalesToCatalog`, `enabledStorage`, `isNewPayment`, `setWholePrice`, `getWholesalesToCSV`, `setSizeMapToData`, `restoreMsg`, `isAdmin`, `convertPrice`, `convertCustomPrice`, `clearProductBlock`, `printReCaptcha`, `checkReCaptcha`, `setLockEntity`, `checkLockEntity`, `unlockEntity`, `addAdminDiscountDetails`, `getAdminDiscountDetails`, `convertCountToHR`, `getWeightUnit`, `getGoogleFonts`, `replaceLetterTemplate`, `accessFullTextSearch`, `sizeTempFiles`, `hasEmoji`, `ajaxResponse`, `getTemplatePlugins`, `decryptLocales`, `genCaptcha`, `response404`, `checkEmail`, `checkIsAutocreatedEmail`, `getVatOptions`, `getMeasureOptions`, `getPaymentObjectOptions`, `getFiscalizationSettings`, `getImageExtension`

### [mogutaApi](https://wiki.moguta.ru/help/Libraries/mogutaApi.html)

`run`

### [Navigator](https://wiki.moguta.ru/help/Libraries/Navigator.html)

`getNumRowsSql`, `getRowsSql`, `getPager`, `getPagerArray`, `checkParamsForPlugins`

### [Page](https://wiki.moguta.ru/help/Libraries/Page.html)

`getParentUrl`, `addPage`, `updatePage`, `delPage`, `getPagesUl`, `getFooterPagesUl`, `getChildPageIds`, `getPagesInside`, `getCategoryTitleList`, `getHierarchyPage`, `getSubPages`, `getParallelslPage`, `getListSubPage`, `getListParallelslPage`, `getTitlePage`, `movePage`, `getPageByUrl`, `getPageById`, `getDesctiption`, `sort`, `changeSortPage`, `refreshVisiblePage`, `getPageInMenu`, `getCountPages`, `getPages`, `getHtmlPageRow`

### [PM](https://wiki.moguta.ru/help/Libraries/PM.html)

`plugLocales`, `getInstance`, `getListShortCode`, `getListNameHooks`, `isHookInReg`, `init`, `registration`, `delete`, `prioritet`, `includePlugins`, `includePluginInFolder`, `getPluginsInfo`, `sortByActivity`, `sortByPluginName`, `readInfo`, `isPluginActive`, `readTemplateInfo`, `getFolderPlugin`, `doShortcode`, `getShortcodeRegex`, `doShortcodeTag`, `createHook`, `shortcodeParseAttrs`, `stripShortcodes`, `stripShortcodeTag`, `downloadPlugin`, `extractPluginZip`, `getPluginDir`, `failtureUpdate`, `checkPluginsUpdate`, `deletePlagin`, `updatePlugin`, `escapeShortcodes`, `hookExists`, `classInfo`, `deactivatePlugin`, `activatePlugin`, `genPluginPath`

### [Property](https://wiki.moguta.ru/help/Libraries/Property.html)

`createProp`, `createPropToCatLink`, `createProductStringProp`, `addDataToProp`, `getHardPropToCsv`, `getEasyPropNameToCsv`, `getEasyPropToCsv`, `createHardPropFromCsv`, `createSizeMapPropFromCsv`, `getPropertyGroup`, `addPropertyGroup`, `deletePropertyGroup`, `sortPropertyToGroup`, `saveUserProperty`, `addCategoryBinds`, `getCountUnusedPropertyValues`, `deleteUnusedPropertyValues`

### [RetailCRM](https://wiki.moguta.ru/help/Libraries/RetailCRM.html)

`createPage`, `saveOptions`, `uploadAll`, `syncAll`, `request`, `processUsers`, `processOrders`, `processRemains`, `updateOrderYur`, `updateOrderName`, `loggActionUpdateOrder`, `editRemains`, `updateOrderProduct`, `getArrKey`, `getArrghKey`, `createUserArr`, `createOrderArr`, `createRemainsArr`, `generateICML`

### [Seo](https://wiki.moguta.ru/help/Libraries/Seo.html)

`getTemplateForMeta`, `getMetaByTemplate`, `autoGenerateSitemap`, `splitSiteMap`, `getXmlView`, `getXmlMainSiteMap`, `deleteSitemapBeforeCreate`, `getMetaByTemplateForAll`

### [SmalCart](https://wiki.moguta.ru/help/Libraries/SmalCart.html)

`getCartData`, `plusPropertyMargin`

### [Storage](https://wiki.moguta.ru/help/Libraries/Storage.html)

`getInstance`, `checkValue`, `save`, `get`, `clear`, `getSessionLifeTime`, `saveSystem`, `getSystem`, `clearSystem`

### [URL](https://wiki.moguta.ru/help/Libraries/URL.html)

`createUrl`, `get`, `getClearUri`, `clearingUrl`, `getCutPath`, `getCountSections`, `getDataUrl`, `getInstance`, `getLastSection`, `getCutSection`, `getQueryParametr`, `getQueryString`, `getSections`, `parseParentUrl`, `parsePageUrl`, `getUri`, `getUrl`, `getRoute`, `isSection`, `post`, `setQueryParametr`, `add_get`, `prepareUrl`, `getDocumentRoot`, `getUrlRedirect`, `clean`, `isAdminAjax`

### [Urlrewrite](https://wiki.moguta.ru/help/Libraries/Urlrewrite.html)

`getInstance`, `init`, `getSeoDataFotUrl`, `getUrlRewriteData`, `setUrlRewrite`, `setActivity`, `deleteRewrite`

### [User](https://wiki.moguta.ru/help/Libraries/User.html)

`getInstance`, `getThis`, `add`, `delete`, `update`, `logout`, `auth`, `checkLockUser`, `lockAuthorization`, `unlock`, `getUserById`, `getUserInfoByEmail`, `getUserInfoByPhone`, `isAuth`, `getListUser`, `getMaxDate`, `getMinDate`, `searchEmail`, `exportToCsvUser`, `access`, `getUserOrderContent`, `getOwners`, `saveLogin`, `getUserEmailByPhone`

### [VKUpload](https://wiki.moguta.ru/help/Libraries/VKUpload.html)

`createPage`, `connect`, `getNum`, `upload`, `dumpPhoto`, `getNumDelete`, `delete`

### [YandexMarket](https://wiki.moguta.ru/help/Libraries/YandexMarket.html)

`newTab`, `saveTab`, `getTab`, `deleteTab`, `prepareUrl`, `getRelated`, `getRelatedNew`, `constructYML`, `getProductDimensions`

## Models

### [Models_Cart](https://wiki.moguta.ru/help/Model/Models_Cart.html)

`addToCart`, `createProperty`, `alreadyInCart`, `delFromCart`, `getListItemId`, `getTotalSumm`, `clearCart`, `refreshCart`, `isEmptyCart`, `getItemsCart`, `repairCart`, `customPrice`, `applyCoupon`

### [Models_Catalog](https://wiki.moguta.ru/help/Model/Models_Catalog.html)

`getCurrentCategory`, `getList`, `getListOld`, `getListByUserFilter`, `getListByUserFilterOld`, `getListProductByKeyWord`, `getListProductByKeyWordOld`, `rowCsvPrintToFile`, `exportToCsv`, `addToCsvLine`, `getCategoryArray`, `getMinPrice`, `getMaxPrice`, `getExampleCategoryCSV`, `getExampleCSV`, `getExampleCsvUpdate`, `filterPublic`, `addPropertyToProduct`, `checkIndexPageBlocks`, `modFilterMinMaxPricesWhere`, `modFilterMinMaxPrices`, `modUserFilterNavigatorSql`

### [Models_Feedback](https://wiki.moguta.ru/help/Model/Models_Feedback.html)

`isValidData`, `getMessage`, `getEmail`, `getFio`

### [Models_Forgotpass](https://wiki.moguta.ru/help/Model/Models_Forgotpass.html)

`getHash`, `sendHashToDB`, `sendUrlToEmail`, `activateUser`

### [Models_OpFieldsCategory](https://wiki.moguta.ru/help/Model/Models_OpFieldsCategory.html)

`getFields`, `getContent`, `saveFields`, `saveContent`

### [Models_OpFieldsOrder](https://wiki.moguta.ru/help/Model/Models_OpFieldsOrder.html)

`fill`, `save`, `createCustomFieldToAdmin`, `get`, `getHumanView`, `getValues`, `checkAdminColumnsTable`, `getFields`, `saveFields`, `getFieldTitle`, `getOrderFormPublicArr`, `getRequiredFields`

### [Models_OpFieldsProduct](https://wiki.moguta.ru/help/Model/Models_OpFieldsProduct.html)

`get`, `fill`, `save`, `getFields`, `saveFields`

### [Models_OpFieldsUser](https://wiki.moguta.ru/help/Model/Models_OpFieldsUser.html)

`fill`, `save`, `createCustomFieldToAdmin`, `get`, `getHumanView`, `getValues`, `checkAdminColumnsTable`, `getFields`, `saveFields`

### [Models_Order](https://wiki.moguta.ru/help/Model/Models_Order.html)

`isValidData`, `addNewUser`, `addOrder`, `sendStatusToEmail`, `updateOrder`, `join1cidProducts`, `refreshCountProducts`, `deleteOrder`, `getOrder`, `setOrderStatus`, `_getHash`, `getDeliveryMethod`, `DeliveryExist`, `getOrderStatus`, `getPaymentMethod`, `getPaymentBlocksMethod`, `getListPayment`, `getMaxPrice`, `getMinPrice`, `getMaxDate`, `getMinDate`, `getListDelivery`, `getPaidedStatus`, `getOrderCount`, `sendMailOfPayed`, `getFileToOrder`, `getFileByMd5`, `sendLinkForElectro`, `sendMailOfUpdateOrder`, `getParamArray`, `cloneOrder`, `getNewOrdersCount`, `getOrderStat`, `getStatisticPeriod`, `printOrder`, `getPdfOrder`, `getMassPdfOrders`, `printQittance`, `getExportCSV`, `refreshCountAfterEdit`, `notSetGoods`, `exportToCsvOrder`, `getOrderDiscount`, `getOrderAdminComments`, `addAdminCommentOrder`, `deleteAdminCommentOrder`, `getCorrectOrderContent`, `getLastOrderId`, `checkOrderReturn`, `printReceipt`, `setPaymentInfoAboutReceipt`, `honestSignGetMarkingCodes`, `honestSignDeleteMarksData`, `honestSignIsMarksHasDuplicate`, `getMarkDuplicate`, `getOrderItemMarkCodes`, `honestSignSetMarksData`, `isOrderNeedSecondReceipt`

### [Models_Payment](https://wiki.moguta.ru/help/Model/Models_Payment.html)

`getPayments`, `getPayment`, `getPaymentById`, `getPaymentByCode`, `getPaymentByPlugin`, `updatePayment`, `createCustomPayment`, `addPayment`, `mergeParams`, `getPaymentsByDeliveryId`, `getDeliveries`, `getPaymentForm`, `getPaymentParams`, `compactParams`, `handleRequest`, `loger`, `isLogsExists`, `togglePaymentLog`, `clearLogs`, `downloadLogs`, `disablePayment`, `deletePluginPayment`, `checkPaymentOutdated`, `getPaymentsIcons`, `checkPaymentForm`, `checkPaymentAvailable`, `getOldPayments`

### [Models_Personal](https://wiki.moguta.ru/help/Model/Models_Personal.html)

`changePass`, `changePhone`

### [Models_Product](https://wiki.moguta.ru/help/Model/Models_Product.html)

`addProduct`, `updateProduct`, `fastUpdateProductVariant`, `importUpdateProductVariant`, `fastUpdateProduct`, `saveVariants`, `cloneProduct`, `cloneImagesProduct`, `deleteProduct`, `deleteImagesFolder`, `deleteImagesProduct`, `getProductByUserFilter`, `getProduct`, `imagesConctruction`, `increaseCountProduct`, `decreaseCountProduct`, `getProductsCount`, `getProductByUrl`, `getProductPrice`, `createPropertyForm`, `getBlockVariants`, `getBlocksVariantsToCatalog`, `addMarginToProp`, `parseMarginToProp`, `calcPrice`, `getVariantImages`, `getVariants`, `noPrintProperty`, `createRelatedForm`, `convertToIso`, `updatePriceCourse`, `deleteImagesVariant`, `prepareImageName`, `setZeroStock`, `movingProductImage`, `recalculateStoragesAll`, `recalculateStoragesById`, `recalculateStorages`, `getProductsTotalCount`, `getProductIdByExternalId`, `updateStorageCount`, `setNewStorageCount`, `deleteStorageRecordsAll`, `deleteStorageRecordsProductOnly`, `deleteStorageRecordsVariantOnly`, `deleteStorageRecordsAllVariants`, `addStorageRecord`, `clearStoragesTable`, `destroyStorageStocks`, `getProductStorageCount`, `getVariantIdByCode`, `getProductStorageData`, `getProductStoragesData`, `getProductStorageTotalCount`, `decreaseCountProductOnStorage`, `orderDecreaseProductStorageCount`, `resetLastUpdate`, `cloneStorageData`, `getStoragesCountsByVariantsIds`, `checkStoragesRecalculation`

### [Models_Registration](https://wiki.moguta.ru/help/Model/Models_Registration.html)

`validDataForm`

## Controllers

### [Controllers_Ajaxrequest](https://wiki.moguta.ru/help/Controller/Controllers_Ajaxrequest.html)

`routeAction`, `routeUserAction`, `checkPathIncludeFile`, `checkAccess`, `delInstal`, `removeDir`

### [Controllers_Api](https://wiki.moguta.ru/help/Controller/Controllers_Api.html)

`test`, `getUsers`, `importUsers`, `deleteUser`, `findUser`, `getCategory`, `importCategory`, `deleteCategory`, `getOrder`, `importOrder`, `deleteOrder`, `getProduct`, `importProduct`, `deleteProduct`, `createCustomFields`

### [Controllers_Cart](https://wiki.moguta.ru/help/Controller/Controllers_Cart.html)

`updateCart`, `delFromCart`, `applyCoupon`

### [Controllers_Catalog](https://wiki.moguta.ru/help/Controller/Controllers_Catalog.html)

`convertLang`, `getSearchData`

### [Controllers_Compare](https://wiki.moguta.ru/help/Controller/Controllers_Compare.html)

`getInfoProducts`

### [Controllers_Enter](https://wiki.moguta.ru/help/Controller/Controllers_Enter.html)

`showCaptcha`, `successfulLogon`, `validForm`

### [Controllers_Exchange1c](https://wiki.moguta.ru/help/Controller/Controllers_Exchange1c.html)

`checkauth`, `success`, `init`, `query`, `ordersUpdate`, `file`, `import`, `extractZip`, `processImportXml`, `updateStorage`, `deleteRootCat`

### [Controllers_Group](https://wiki.moguta.ru/help/Controller/Controllers_Group.html)

`getGroupsData`

### [Controllers_Order](https://wiki.moguta.ru/help/Controller/Controllers_Order.html)

`getPaymentView`, `getPaymentViewFile`, `confirmOrder`, `getDelivery`, `getPayment`, `getDeliveryOrderOptions`, `getPaymentByDeliveryIdOld`, `setPaymentRate`, `applyRate`, `getEssentialElements`, `includeIconsPack`

### [Controllers_Payment](https://wiki.moguta.ru/help/Controller/Controllers_Payment.html)

`actionWhenPayment`

### [Controllers_Registration](https://wiki.moguta.ru/help/Controller/Controllers_Registration.html)

`unValidForm`

## Hook names

The [official hook reference](https://wiki.moguta.ru/help/Hooks) documented 112 hook names at snapshot time. Hook matching is
case-sensitive in practice; use the exact installed hook string.

### Core lifecycle and MG hooks

`mg_start`, `mg_end`, `MG_getHtmlContent`, `MG_getPhpContent`, `MG_meta`, `MG_getBuffer`, `MG_seoMeta`, `MG_createInformerPanel`, `MG_logReffererInfo`, `MG_layoutManager`, `MG_loadLocaleData`, `MG_loadCountFromStorageToCatalog`, `MG_loadWholeSalesToCatalog`

### Model hooks

`Models_Cart_addToCart`, `Models_Cart_alreadyInCart`, `Models_Cart_delFromCart`, `Models_Cart_getTotalSumm`, `Models_Cart_refreshCart`, `Models_Cart_isEmptyCart`, `Models_Cart_getItemsCart`, `Models_Cart_customPrice`, `Models_Cart_applyCoupon`, `Models_Catalog_getCurrentCategory`, `Models_Catalog_getList`, `Models_Catalog_getListOld`, `Models_Catalog_getListByUserFilter`, `Models_Catalog_getListByUserFilterOld`, `Models_Catalog_getListProductByKeyWord`, `Models_Catalog_getListProductByKeyWordOld`, `Models_Catalog_filterPublic`, `Models_Catalog_checkIndexPageBlocks`, `Models_Catalog_modFilterMinMaxPricesWhere`, `Models_Catalog_modFilterMinMaxPrices`, `Models_Catalog_modUserFilterNavigatorSql`, `Models_Feedback_isValidData`, `Models_Order_isValidData`, `Models_Order_addOrder`, `Models_Order_sendStatusToEmail`, `Models_Order_updateOrder`, `Models_Order_refreshCountProducts`, `Models_Order_deleteOrder`, `Models_Order_setOrderStatus`, `Models_Order_sendMailOfPayed`, `Models_Order_cloneOrder`, `Models_Order_refreshCountAfterEdit`, `Models_Order_notSetGoods`, `Models_Order_getOrderDiscount`, `Models_Order_printReceipt`, `Models_Payment_handleRequest`, `Models_Payment_deletePluginPayment`, `Models_Personal_changePass`, `Models_Personal_changePhone`, `Models_Product_addProduct`, `Models_Product_updateProduct`, `Models_Product_fastUpdateProduct`, `Models_Product_cloneProduct`, `Models_Product_deleteProduct`, `Models_Product_getProduct`, `Models_Product_imagesConctruction`, `Models_Product_getProductByUrl`, `Models_Product_createPropertyForm`, `Models_Product_getVariants`, `Models_Product_createRelatedForm`, `Models_Registration_validDataForm`

### Controller hooks

`Controllers_Payment_actionWhenPayment`

### Library and admin hooks

`getAdminOrderForm`, `adminOrderDiscountPrepareData`, `adminOrderSavePrepareData`, `Category_addCategory`, `Category_updateCategory`, `Category_delCategory`, `Category_getCategoriesHTML`, `Category_getCategoriesHorHTML`, `Category_getCategoryListUl`, `Category_getCategoryList`, `Category_getCategoryTitleList`, `Category_getInsideCategory`, `Category_getHierarchyCategory`, `Category_getTitleCategory`, `Category_getCategoryByUrl`, `Category_getCategoryById`, `Category_getDesctiption`, `Delivery_getDeliveryById`, `Filter_getFilterSql`, `Filter_getProductIdByFilter`, `Filter_getApplyFilterList`, `Mailer_setSMTPDataConnect`, `Menu_getMenuFull`, `Menu_getMenu`, `Navigator_checkParamsForPlugins`, `Page_addPage`, `Page_updatePage`, `Page_delPage`, `Page_getPagesUl`, `Page_getFooterPagesUl`, `Page_getPagesInside`, `Page_getHierarchyPage`, `Page_getTitlePage`, `Page_getPageByUrl`, `Page_getPageById`, `Page_getPageInMenu`, `SmalCart_getCartData`, `Storage_checkValue`, `Urlrewrite_getUrlRewriteData`, `User_add`, `User_delete`, `User_update`, `User_auth`, `User_getUserById`, `User_getUserInfoByEmail`, `User_getUserInfoByPhone`, `User_getListUser`
