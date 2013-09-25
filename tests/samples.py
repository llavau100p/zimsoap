#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Zimbra XML samples, for unit-testing.

MISNAMED_DOMAIN="""<demain id="b37d6b98-dc8c-474a-9243-f5dfc3ecf6ac" name="client1.unbound.oasiswork.fr">
                <a n="zimbraGalLdapPageSize">1000</a>
                <a n="zimbraAggregateQuotaLastUsage">401</a>
                <a n="zimbraInternalSharingCrossDomainEnabled">TRUE</a>
                <a n="zimbraMailStatus">enabled</a>
                <a n="zimbraGalSyncTimestampFormat">yyyyMMddHHmmss'Z'</a>
                <a n="zimbraGalSyncLdapPageSize">1000</a>
                <a n="zimbraZimletDataSensitiveInMixedModeDisabled">TRUE</a>
                <a n="zimbraId">b37d6b98-dc8c-474a-9243-f5dfc3ecf6ac</a>
                <a n="zimbraAdminConsoleCatchAllAddressEnabled">FALSE</a>
                <a n="zimbraGalMaxResults">100</a>
                <a n="zimbraDomainAggregateQuotaWarnPercent">80</a>
                <a n="zimbraAutoProvNotificationBody">Your account has been auto provisioned. Your email address is ${ACCOUNT_ADDRESS}.</a>
                <a n="zimbraGalGroupIndicatorEnabled">TRUE</a>
                <a n="zimbraDomainMandatoryMailSignatureEnabled">FALSE</a>
                <a n="zimbraGalSyncMaxConcurrentClients">2</a>
                <a n="zimbraReverseProxyClientCertMode">off</a>
                <a n="zimbraCreateTimestamp">20130910123204Z</a>
                <a n="zimbraLdapGalSyncDisabled">FALSE</a>
                <a n="dc">client1</a>
                <a n="zimbraGalInternalSearchBase">DOMAIN</a>
                <a n="zimbraGalLdapValueMap">zimbraAccountCalendarUserType: Room|Equipment RESOURCE</a>
                <a n="zimbraGalLdapValueMap">zimbraCalResType: Room Location</a>
                <a n="zimbraExternalShareInvitationUrlExpiration">0</a>
                <a n="objectClass">dcObject</a>
                <a n="objectClass">organization</a>
                <a n="objectClass">zimbraDomain</a>
                <a n="objectClass">amavisAccount</a>
                <a n="zimbraFreebusyExchangeCachedIntervalStart">7d</a>
                <a n="zimbraDomainAggregateQuotaPolicy">ALLOWSENDRECEIVE</a>
                <a n="zimbraDomainName">client1.unbound.oasiswork.fr</a>
                <a n="zimbraDomainStatus">active</a>
                <a n="zimbraDomainType">local</a>
                <a n="zimbraAdminConsoleLDAPAuthEnabled">FALSE</a>
                <a n="zimbraGalLdapAttrMap">(binary) userSMIMECertificate=userSMIMECertificate</a>
                <a n="zimbraGalLdapAttrMap">(certificate) userCertificate=userCertificate</a>
            </demain>"""

SIMPLE_DOMAIN="""<domain id="b37d6b98-dc8c-474a-9243-f5dfc3ecf6ac" name="client1.unbound.oasiswork.fr">
				<a n="zimbraGalLdapPageSize">1000</a>
				<a n="zimbraAggregateQuotaLastUsage">401</a>
				<a n="zimbraInternalSharingCrossDomainEnabled">TRUE</a>
				<a n="zimbraMailStatus">enabled</a>
				<a n="zimbraGalSyncTimestampFormat">yyyyMMddHHmmss'Z'</a>
				<a n="zimbraGalSyncLdapPageSize">1000</a>
				<a n="zimbraZimletDataSensitiveInMixedModeDisabled">TRUE</a>
				<a n="zimbraId">b37d6b98-dc8c-474a-9243-f5dfc3ecf6ac</a>
				<a n="zimbraAdminConsoleCatchAllAddressEnabled">FALSE</a>
				<a n="zimbraGalMaxResults">100</a>
				<a n="zimbraMailSSLClientCertPrincipalMap">SUBJECT_EMAILADDRESS=name</a>
				<a n="zimbraDomainAggregateQuotaWarnPercent">80</a>
				<a n="zimbraAutoProvNotificationBody">Your account has been auto provisioned.  Your email address is ${ACCOUNT_ADDRESS}.</a>
				<a n="zimbraGalGroupIndicatorEnabled">TRUE</a>
				<a n="zimbraDomainMandatoryMailSignatureEnabled">FALSE</a>
				<a n="zimbraGalSyncMaxConcurrentClients">2</a>
				<a n="zimbraReverseProxyClientCertMode">off</a>
				<a n="zimbraCreateTimestamp">20130910123204Z</a>
				<a n="zimbraLdapGalSyncDisabled">FALSE</a>
				<a n="dc">client1</a>
				<a n="zimbraGalInternalSearchBase">DOMAIN</a>
				<a n="zimbraGalLdapValueMap">zimbraAccountCalendarUserType: Room|Equipment RESOURCE</a>
				<a n="zimbraGalLdapValueMap">zimbraCalResType: Room Location</a>
				<a n="zimbraExternalShareInvitationUrlExpiration">0</a>
				<a n="objectClass">dcObject</a>
				<a n="objectClass">organization</a>
				<a n="objectClass">zimbraDomain</a>
				<a n="objectClass">amavisAccount</a>
				<a n="zimbraFreebusyExchangeCachedIntervalStart">7d</a>
				<a n="zimbraDomainAggregateQuotaPolicy">ALLOWSENDRECEIVE</a>
				<a n="zimbraDomainName">client1.unbound.oasiswork.fr</a>
				<a n="zimbraDomainStatus">active</a>
				<a n="zimbraDomainType">local</a>
				<a n="zimbraAdminConsoleLDAPAuthEnabled">FALSE</a>
				<a n="zimbraGalLdapAttrMap">(binary) userSMIMECertificate=userSMIMECertificate</a>
				<a n="zimbraGalLdapAttrMap">(certificate) userCertificate=userCertificate</a>
				<a n="zimbraGalLdapAttrMap">co=workCountry</a>
				<a n="zimbraGalLdapAttrMap">company=company</a>
				<a n="zimbraGalLdapAttrMap">description=notes</a>
				<a n="zimbraGalLdapAttrMap">displayName,cn=fullName,fullName2,fullName3,fullName4,fullName5,fullName6,fullName7,fullName8,fullName9,fullName10</a>
				<a n="zimbraGalLdapAttrMap">facsimileTelephoneNumber,fax=workFax</a>
				<a n="zimbraGalLdapAttrMap">givenName,gn=firstName</a>
				<a n="zimbraGalLdapAttrMap">homeTelephoneNumber,homePhone=homePhone</a>
				<a n="zimbraGalLdapAttrMap">initials=initials</a>
				<a n="zimbraGalLdapAttrMap">l=workCity</a>
				<a n="zimbraGalLdapAttrMap">mobileTelephoneNumber,mobile=mobilePhone</a>
				<a n="zimbraGalLdapAttrMap">msExchResourceSearchProperties=zimbraAccountCalendarUserType</a>
				<a n="zimbraGalLdapAttrMap">objectClass=objectClass</a>
				<a n="zimbraGalLdapAttrMap">ou=department</a>
				<a n="zimbraGalLdapAttrMap">pagerTelephoneNumber,pager=pager</a>
				<a n="zimbraGalLdapAttrMap">physicalDeliveryOfficeName=office</a>
				<a n="zimbraGalLdapAttrMap">postalCode=workPostalCode</a>
				<a n="zimbraGalLdapAttrMap">sn=lastName</a>
				<a n="zimbraGalLdapAttrMap">st=workState</a>
				<a n="zimbraGalLdapAttrMap">street,streetAddress=workStreet</a>
				<a n="zimbraGalLdapAttrMap">telephoneNumber=workPhone</a>
				<a n="zimbraGalLdapAttrMap">title=jobTitle</a>
				<a n="zimbraGalLdapAttrMap">whenChanged,modifyTimeStamp=modifyTimeStamp</a>
				<a n="zimbraGalLdapAttrMap">whenCreated,createTimeStamp=createTimeStamp</a>
				<a n="zimbraGalLdapAttrMap">zimbraCalResBuilding=zimbraCalResBuilding</a>
				<a n="zimbraGalLdapAttrMap">zimbraCalResCapacity,msExchResourceCapacity=zimbraCalResCapacity</a>
				<a n="zimbraGalLdapAttrMap">zimbraCalResContactEmail=zimbraCalResContactEmail</a>
				<a n="zimbraGalLdapAttrMap">zimbraCalResFloor=zimbraCalResFloor</a>
				<a n="zimbraGalLdapAttrMap">zimbraCalResLocationDisplayName=zimbraCalResLocationDisplayName</a>
				<a n="zimbraGalLdapAttrMap">zimbraCalResSite=zimbraCalResSite</a>
				<a n="zimbraGalLdapAttrMap">zimbraCalResType,msExchResourceSearchProperties=zimbraCalResType</a>
				<a n="zimbraGalLdapAttrMap">zimbraDistributionListSubscriptionPolicy=zimbraDistributionListSubscriptionPolicy</a>
				<a n="zimbraGalLdapAttrMap">zimbraDistributionListUnsubscriptionPolicy=zimbraDistributionListUnsubscriptionPolicy</a>
				<a n="zimbraGalLdapAttrMap">zimbraId=zimbraId</a>
				<a n="zimbraGalLdapAttrMap">zimbraMailDeliveryAddress,zimbraMailAlias,mail=email,email2,email3,email4,email5,email6,email7,email8,email9,email10,email11,email12,email13,email14,email15,email16</a>
				<a n="zimbraGalLdapAttrMap">zimbraMailForwardingAddress=member</a>
				<a n="zimbraGalLdapAttrMap">zimbraPhoneticCompany,ms-DS-Phonetic-Company-Name=phoneticCompany</a>
				<a n="zimbraGalLdapAttrMap">zimbraPhoneticFirstName,ms-DS-Phonetic-First-Name=phoneticFirstName</a>
				<a n="zimbraGalLdapAttrMap">zimbraPhoneticLastName,ms-DS-Phonetic-Last-Name=phoneticLastName</a>
				<a n="zimbraWebClientMaxInputBufferLength">1024</a>
				<a n="zimbraGalMode">zimbra</a>
				<a n="zimbraSkinLogoURL">http://www.zimbra.com</a>
				<a n="zimbraMailDomainQuota">0</a>
				<a n="zimbraGalAlwaysIncludeLocalCalendarResources">FALSE</a>
				<a n="zimbraBasicAuthRealm">Zimbra Client 1</a>
				<a n="zimbraGalAccountId">ed868032-bd7f-40f5-a87e-ddf67c835682</a>
				<a n="zimbraAdminConsoleDNSCheckEnabled">FALSE</a>
				<a n="zimbraAuthMech">zimbra</a>
				<a n="zimbraFreebusyExchangeCachedInterval">60d</a>
				<a n="zimbraGalTokenizeAutoCompleteKey">and</a>
				<a n="zimbraDomainAggregateQuota">0</a>
				<a n="zimbraAutoProvNotificationSubject">New account auto provisioned</a>
				<a n="zimbraGalAutoCompleteLdapFilter">externalLdapAutoComplete</a>
				<a n="zimbraMobileMetadataMaxSizeEnabled">FALSE</a>
				<a n="zimbraAdminConsoleSkinEnabled">FALSE</a>
				<a n="o">client1.unbound.oasiswork.fr domain</a>
				<a n="zimbraGalTokenizeSearchKey">and</a>
				<a n="zimbraFileUploadMaxSizePerFile">2147483648</a>
				<a n="zimbraGalDefinitionLastModifiedTime">20130910123204Z</a>
				<a n="zimbraFreebusyExchangeServerType">webdav</a>
				<a n="zimbraAutoProvBatchSize">20</a>
			</domain>

"""

MBOX = """<mbox accountId="d78fd9c9-f000-440b-bce6-ea938d40fa2d" changeCheckPoint="4000" contactCount="0" groupId="6" id="6" indexVolumeId="2" itemIdCheckPoint="256" lastSoapAccess="0" newMessages="0" sizeCheckPoint="0" trackingImap="0" trackingSync="0"/>"""

DISTRIBUTION_LIST = """
<dl dynamic="0" id="4d97616d-53fd-4744-8535-64e6a0776df1" name="newlist@client1.unbound.oasiswork.fr">
	<a n="uid">newlist</a>
	<a n="mail">newlist@client1.unbound.oasiswork.fr</a>
	<a n="zimbraMailStatus">enabled</a>
	<a n="zimbraMailHost">zimbratest.saas.oasiswork.fr</a>
	<a n="zimbraId">4d97616d-53fd-4744-8535-64e6a0776df1</a>
	<a n="zimbraCreateTimestamp">20130924150950Z</a>
	<a n="objectClass">zimbraDistributionList</a>
	<a n="objectClass">zimbraMailRecipient</a>
	<a n="zimbraMailAlias">newlist@client1.unbound.oasiswork.fr</a>
</dl>

"""