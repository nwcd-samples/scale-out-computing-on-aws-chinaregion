'''
# AWS::ControlTower Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_controltower as controltower
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for ControlTower construct libraries](https://constructs.dev/search?q=controltower)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::ControlTower resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_ControlTower.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::ControlTower](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_ControlTower.html).

(Read the [CDK Contributing Guide](https://github.com/aws/aws-cdk/blob/main/CONTRIBUTING.md) and submit an RFC if you are interested in contributing to this construct library.)

<!--END CFNONLY DISCLAIMER-->
'''
import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from typeguard import check_type

from .._jsii import *

import constructs as _constructs_77d1e7e8
from .. import (
    CfnResource as _CfnResource_9df397a6,
    CfnTag as _CfnTag_f6864754,
    IInspectable as _IInspectable_c2943556,
    TreeInspector as _TreeInspector_488e0dd5,
)


@jsii.implements(_IInspectable_c2943556)
class CfnEnabledControl(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_controltower.CfnEnabledControl",
):
    '''The resource represents an enabled control.

    It specifies an asynchronous operation that creates AWS resources on the specified organizational unit and the accounts it contains. The resources created will vary according to the control that you specify.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-controltower-enabledcontrol.html
    :cloudformationResource: AWS::ControlTower::EnabledControl
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_controltower as controltower
        
        cfn_enabled_control = controltower.CfnEnabledControl(self, "MyCfnEnabledControl",
            control_identifier="controlIdentifier",
            target_identifier="targetIdentifier"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        control_identifier: builtins.str,
        target_identifier: builtins.str,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param control_identifier: The ARN of the control. Only *Strongly recommended* and *Elective* controls are permitted, with the exception of the *Region deny* control. For information on how to find the ``controlIdentifier`` , see `the overview page <https://docs.aws.amazon.com//controltower/latest/APIReference/Welcome.html>`_ .
        :param target_identifier: The ARN of the organizational unit. For information on how to find the ``targetIdentifier`` , see `the overview page <https://docs.aws.amazon.com//controltower/latest/APIReference/Welcome.html>`_ .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1f147c3cf3aed5100105feba92fb41fa040a90e250e566c4f852830a75cfc586)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnEnabledControlProps(
            control_identifier=control_identifier, target_identifier=target_identifier
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f48fb910d3eecb04d51dd6fcc7cb9241b6efe5d9c5090dd7e2fd56008e8b927d)
            check_type(argname="argument inspector", value=inspector, expected_type=type_hints["inspector"])
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__261484f697e7db6197c5dc87066a21bee7f59b77e85daa6773dbaf62c8d80eea)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="controlIdentifier")
    def control_identifier(self) -> builtins.str:
        '''The ARN of the control.'''
        return typing.cast(builtins.str, jsii.get(self, "controlIdentifier"))

    @control_identifier.setter
    def control_identifier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f8a36ed174761f649221cc9963f7efb537dbfdcc36152637e5c027b145c88fbe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "controlIdentifier", value)

    @builtins.property
    @jsii.member(jsii_name="targetIdentifier")
    def target_identifier(self) -> builtins.str:
        '''The ARN of the organizational unit.'''
        return typing.cast(builtins.str, jsii.get(self, "targetIdentifier"))

    @target_identifier.setter
    def target_identifier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e9224f8582867a991a7807db81df627cf779770c76fc707cfecf8fd568b7998a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetIdentifier", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_controltower.CfnEnabledControlProps",
    jsii_struct_bases=[],
    name_mapping={
        "control_identifier": "controlIdentifier",
        "target_identifier": "targetIdentifier",
    },
)
class CfnEnabledControlProps:
    def __init__(
        self,
        *,
        control_identifier: builtins.str,
        target_identifier: builtins.str,
    ) -> None:
        '''Properties for defining a ``CfnEnabledControl``.

        :param control_identifier: The ARN of the control. Only *Strongly recommended* and *Elective* controls are permitted, with the exception of the *Region deny* control. For information on how to find the ``controlIdentifier`` , see `the overview page <https://docs.aws.amazon.com//controltower/latest/APIReference/Welcome.html>`_ .
        :param target_identifier: The ARN of the organizational unit. For information on how to find the ``targetIdentifier`` , see `the overview page <https://docs.aws.amazon.com//controltower/latest/APIReference/Welcome.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-controltower-enabledcontrol.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_controltower as controltower
            
            cfn_enabled_control_props = controltower.CfnEnabledControlProps(
                control_identifier="controlIdentifier",
                target_identifier="targetIdentifier"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__23e0009029d159859294a7c6bf2b14974d61fd34884bdb5a993abbb2d14cff4f)
            check_type(argname="argument control_identifier", value=control_identifier, expected_type=type_hints["control_identifier"])
            check_type(argname="argument target_identifier", value=target_identifier, expected_type=type_hints["target_identifier"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "control_identifier": control_identifier,
            "target_identifier": target_identifier,
        }

    @builtins.property
    def control_identifier(self) -> builtins.str:
        '''The ARN of the control.

        Only *Strongly recommended* and *Elective* controls are permitted, with the exception of the *Region deny* control. For information on how to find the ``controlIdentifier`` , see `the overview page <https://docs.aws.amazon.com//controltower/latest/APIReference/Welcome.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-controltower-enabledcontrol.html#cfn-controltower-enabledcontrol-controlidentifier
        '''
        result = self._values.get("control_identifier")
        assert result is not None, "Required property 'control_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def target_identifier(self) -> builtins.str:
        '''The ARN of the organizational unit.

        For information on how to find the ``targetIdentifier`` , see `the overview page <https://docs.aws.amazon.com//controltower/latest/APIReference/Welcome.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-controltower-enabledcontrol.html#cfn-controltower-enabledcontrol-targetidentifier
        '''
        result = self._values.get("target_identifier")
        assert result is not None, "Required property 'target_identifier' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEnabledControlProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnLandingZone(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_controltower.CfnLandingZone",
):
    '''Definition of AWS::ControlTower::LandingZone Resource Type.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-controltower-landingzone.html
    :cloudformationResource: AWS::ControlTower::LandingZone
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_controltower as controltower
        
        cfn_landing_zone = controltower.CfnLandingZone(self, "MyCfnLandingZone",
            version="version",
        
            # the properties below are optional
            tags=[CfnTag(
                key="key",
                value="value"
            )]
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        version: builtins.str,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param version: 
        :param tags: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__af3c2c6625c6aae1afd50bbbd83dafe3289d77c3e128938fa7a5e5c8c7ddf150)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnLandingZoneProps(version=version, tags=tags)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b0d56a7dc8ba80b56dd66a841e7e3da6e2e5ff196ed627e202ce0b501f32afe2)
            check_type(argname="argument inspector", value=inspector, expected_type=type_hints["inspector"])
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bdedd2a6b11698e1ddadd84cf4edea18986d77eb329c8e69790ef015dc016ac0)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrDriftStatus")
    def attr_drift_status(self) -> builtins.str:
        '''
        :cloudformationAttribute: DriftStatus
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDriftStatus"))

    @builtins.property
    @jsii.member(jsii_name="attrLandingZoneIdentifier")
    def attr_landing_zone_identifier(self) -> builtins.str:
        '''
        :cloudformationAttribute: LandingZoneIdentifier
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLandingZoneIdentifier"))

    @builtins.property
    @jsii.member(jsii_name="attrLatestAvailableVersion")
    def attr_latest_available_version(self) -> builtins.str:
        '''
        :cloudformationAttribute: LatestAvailableVersion
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLatestAvailableVersion"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''
        :cloudformationAttribute: Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "version"))

    @version.setter
    def version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e32b3e7b64f2950f24c12755b01848b9ebe791c11c2152b740f8f62257157e39)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "version", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__74f7c6529f7d31ad5ed3d98ad190f8c0fed87380c25f04fc3e960c88ff73bdaf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_controltower.CfnLandingZoneProps",
    jsii_struct_bases=[],
    name_mapping={"version": "version", "tags": "tags"},
)
class CfnLandingZoneProps:
    def __init__(
        self,
        *,
        version: builtins.str,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnLandingZone``.

        :param version: 
        :param tags: 

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-controltower-landingzone.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_controltower as controltower
            
            cfn_landing_zone_props = controltower.CfnLandingZoneProps(
                version="version",
            
                # the properties below are optional
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__19c72c4436a305fc4b4dfd189564d877d145ce92e0c75f37eafddc778100f13e)
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "version": version,
        }
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def version(self) -> builtins.str:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-controltower-landingzone.html#cfn-controltower-landingzone-version
        '''
        result = self._values.get("version")
        assert result is not None, "Required property 'version' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-controltower-landingzone.html#cfn-controltower-landingzone-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLandingZoneProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnEnabledControl",
    "CfnEnabledControlProps",
    "CfnLandingZone",
    "CfnLandingZoneProps",
]

publication.publish()

def _typecheckingstub__1f147c3cf3aed5100105feba92fb41fa040a90e250e566c4f852830a75cfc586(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    control_identifier: builtins.str,
    target_identifier: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f48fb910d3eecb04d51dd6fcc7cb9241b6efe5d9c5090dd7e2fd56008e8b927d(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__261484f697e7db6197c5dc87066a21bee7f59b77e85daa6773dbaf62c8d80eea(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f8a36ed174761f649221cc9963f7efb537dbfdcc36152637e5c027b145c88fbe(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e9224f8582867a991a7807db81df627cf779770c76fc707cfecf8fd568b7998a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__23e0009029d159859294a7c6bf2b14974d61fd34884bdb5a993abbb2d14cff4f(
    *,
    control_identifier: builtins.str,
    target_identifier: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af3c2c6625c6aae1afd50bbbd83dafe3289d77c3e128938fa7a5e5c8c7ddf150(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    version: builtins.str,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b0d56a7dc8ba80b56dd66a841e7e3da6e2e5ff196ed627e202ce0b501f32afe2(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bdedd2a6b11698e1ddadd84cf4edea18986d77eb329c8e69790ef015dc016ac0(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e32b3e7b64f2950f24c12755b01848b9ebe791c11c2152b740f8f62257157e39(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__74f7c6529f7d31ad5ed3d98ad190f8c0fed87380c25f04fc3e960c88ff73bdaf(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__19c72c4436a305fc4b4dfd189564d877d145ce92e0c75f37eafddc778100f13e(
    *,
    version: builtins.str,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
